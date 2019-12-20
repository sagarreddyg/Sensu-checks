import requests
import sys


def get_listof_hosts():
    host=[]
    with open("List.txt", "r+") as file:
        for line in file:
            host.append("{}".format(line[:-1]),)
    return host


host = get_listof_hosts()
count  = 0
for i in range(len(host)):
    req = requests.get(host[i])
    if req.status_code == 200:
        print("OK : {} is responding time:{}".format(req.url,req.elapsed))
    else:
        print("{} is not responding with code {} time:{}".format(req.url, req.status_code, req.elapsed))
        count += 1
if count == 0:
    sys.exit(0)
else:
    sys.exit(2)

