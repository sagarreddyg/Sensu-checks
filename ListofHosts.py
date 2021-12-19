import os
import re
import requests


def get_listof_criticalhosts():
    host=[]
    fh = open("List.txt", "r")
    lines = fh.readlines()
    fh.close()
    os.remove('List.txt')
    # Weed out blank lines with filter
    lines = filter(lambda x: not x.isspace(), lines)
    # Write
    fh = open("List.txt", "w")
    fh.write("".join(lines))
    # should also work instead of joining the list:
    # fh.writelines(lines)
    fh.close()
    with open("List.txt", "r+") as file:
        for line in file:
            host.append("{}".format(re.sub(r"\s+", "", line[:-1])),)
    return host


HOSTS = []
cri = get_listof_criticalhosts()


"""def UpdateList(urlcount, url):
    file = open("List.txt", "r")
    lines = file.readlines()
    file.close()
    del lines[urlcount]
    file = open("List.txt", "w")
    for l in lines:
        file.write(l)
    file.close()
    file = open("UnknownList.txt", "a")
    file.write(url)
    file.write("\n")
    file.close()
"""

for i in range(len(cri)):
    HOSTS.append((cri[i], 443))
    """
    try:
        code = requests.get('http://{}'.format(cri[i]))
        if 100 <= code.status_code >= 499:
            print("The url is not responding {0}, status code is {1}".format(cri[i], code.status_code))
        else:
            HOSTS.append((cri[i], 443))
    except:
        continue"""


