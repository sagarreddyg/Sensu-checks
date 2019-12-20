#! /usr/bin/python3
# -*- encoding: utf-8 -*-
# requires a recent enough python with idna support in socket
# pyopenssl, cryptography and idna
# check config sensuctl check create check_name --commamd 'file location' --interval 30 --subscriptions subscriptionname
#This check will alerts every 30 seconds and gives the output for ssl certificate expiration date
#Warning : 100 days
#Critical : 30 days
import os
import concurrent.futures
from OpenSSL import SSL
import idna
import datetime
from socket import socket
from collections import namedtuple
from datetime import date
import ListofHosts

HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
# ('www.bestprice.in', 443)

HOSTS = ListofHosts.HOSTS

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


def get_criticalhosts():
    criticalhost=[]
    with open("Critical.txt", "r+") as file:
        for line in file:
            criticalhost.append((line[:-1],443))
    file.close()
    return criticalhost


def timeinfo():
    da = datetime.date.today()
    d1 = date(hostinfo.cert.not_valid_after.year, hostinfo.cert.not_valid_after.month,
              hostinfo.cert.not_valid_after.day)
    d2 = date(da.year, da.month, da.day)
    return d1 - d2


def critical(hostinfo):
    exdays = timeinfo()
    if exdays.days < 300:
        ListofHosts.update_criticalhosts(hostinfo.hostname)



def check_it_out(hostname, port):
    hostinfo = get_certificate(hostname, port)


if __name__ == '__main__':
    os.remove('Critical.txt')
    fi = open('Critical.txt', 'w')
    fi.close()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        for hostinfo in e.map(lambda x: get_certificate(x[0], x[1]), HOSTS):
            exdays = timeinfo()
            if exdays.days <= 300:
                critical(hostinfo)
            else:
                delli = get_criticalhosts()
                for i in range(len(delli)):
                    if hostinfo.hostname in delli and hostinfo.hostname not in ListofHosts.HOSTS:
                        if len(delli)<=0:
                            break
                        else:
                            delli.remove(delli[i])
                        ListofHosts.update_criticalhosts(delli)

print("Critical.txt updated..")
