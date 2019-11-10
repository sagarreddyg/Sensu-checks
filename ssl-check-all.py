#! /usr/bin/pythom3
# -*- encoding: utf-8 -*-
# requires a recent enough python with idna support in socket
# pyopenssl, cryptography and idna
# check config sensuctl check create check_name --commamd 'file location' --interval 30 --subscriptions subscriptionname
#This check will alerts every 30 seconds and gives the output for ssl certificate expiration date
#Warning : 100 days
#Critical : 30 days

from OpenSSL import SSL
from cryptography import x509
from cryptography.x509.oid import NameOID
import idna
import datetime
from socket import socket
from collections import namedtuple
from datetime import date
import sys


HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
# ('www.bestprice.in', 443)
HOSTS = [
    ('www.capillarytech.com', 443),
    ('www.pizzahut.co.za', 443),
    ('mon-dashboard.capillarytech.cn.com', 443),
    ('www.gait.com.kw', 443),
    ('www.bestprice.in', 443),
    ('www.capillarytech.com', 443),
    ('phindia-resources.cdn.martjack.io', 443)
]


def verify_cert(cert, hostname):
    # verify notAfter/notBefore, CA trusted, servername/sni/hostname
    cert.has_expired()
    # service_identity.pyopenssl.verify_hostname(client_ssl, hostname)
    # issuer


def get_certificate(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()

    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD)  # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()

    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)


def get_alt_names(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return ext.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        return None


def get_common_name(cert):
    try:
        names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None


def get_issuer(cert):
    try:
        names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None


def Printinfo():

    return (''' » {hostname} « … {peername}
                \tcommonName: {commonname}
                \tSAN: {SAN}
                \tissuer: {issuer}
                '''.format(
                hostname=hostinfo.hostname,
                peername=hostinfo.peername,
                commonname=get_common_name(hostinfo.cert),
                SAN=get_alt_names(hostinfo.cert),
                issuer=get_issuer(hostinfo.cert),
            ))

def critical(hostinfo, Printinfo):
    da = datetime.date.today()
    d1 = date(hostinfo.cert.not_valid_after.year, hostinfo.cert.not_valid_after.month,
              hostinfo.cert.not_valid_after.day)
    d2 = date(da.year, da.month, da.day)
    daysi = d1 - d2
    exdays = daysi

    if exdays.days < 10:
        if exdays.days < 0:
            print("Critical : SSL Certificate for {} is expired on {} days: {} \n{}".format(hostinfo.hostname,
                                                                                            hostinfo.cert.not_valid_after,
                                                                                            daysi.days, Printinfo))
        if 0 <= exdays.days <= 10:
            print("Critical : SSL Certificate for {} will expire on {} days: {} \n{}".format(hostinfo.hostname,
                                                                                            hostinfo.cert.not_valid_after,
                                                                                            daysi.days, Printinfo))

def warning(hostinfo, Printinfo):
    da = datetime.date.today()
    d1 = date(hostinfo.cert.not_valid_after.year, hostinfo.cert.not_valid_after.month,
              hostinfo.cert.not_valid_after.day)
    d2 = date(da.year, da.month, da.day)
    daysi = d1 - d2
    exdays = daysi
    if 10 < exdays.days <= 100:
        print("Warning : SSL Certificate for {} is expired on {} days: {} \n{}".format(hostinfo.hostname,
                                                                                        hostinfo.cert.not_valid_after,
                                                                                        daysi.days, Printinfo))

def check_it_out(hostname, port):
    hostinfo = get_certificate(hostname, port)


import concurrent.futures

if __name__ == '__main__':
    criticalcount = 0
    warningcount = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        for hostinfo in e.map(lambda x: get_certificate(x[0], x[1]), HOSTS):
            da = datetime.date.today()
            d1 = date(hostinfo.cert.not_valid_after.year, hostinfo.cert.not_valid_after.month,
                      hostinfo.cert.not_valid_after.day)
            d2 = date(da.year, da.month, da.day)
            daysi = d1 - d2
            exdays = daysi
            if exdays.days <= 30:
                critical(hostinfo, Printinfo())
                criticalcount += 1
            if exdays.days <= 100:
                warning(hostinfo, Printinfo())
                warningcount += 1
    if criticalcount >=1:
        sys.exit(2)
    elif warningcount >=1:
        sys.exit(1)
    else:
        print("OK : All sll certificate are up to date")
        sys.exit(0)
