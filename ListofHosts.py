import os


def get_listof_criticalhosts():
    host=[]
    with open("List.txt", "r+") as file:
        for line in file:
            host.append("{}".format(line[:-1]),)
    return host


HOSTS = []
cri = get_listof_criticalhosts()
for i in range(len(cri)):
    HOSTS.append((cri[i], 443))


def create_criticalhosts(host):
    for l in range(len(HOSTS)):
        with open("Critical.txt", "r+") as file:
            for line in file:
                if host[l][0] in line:
                    break
            else:  # not found, we are at the eof
                file.write('{},\n'.format(host[l]))  # append missing datd
        file.close()


def get_listof_criticalhosts():
    host=[]
    with open("Critical.txt", "r+") as file:
        for line in file:
            host.append("{}".format(line[:-1]),)
    return host


def update_criticalhosts(host):
    with open("Critical.txt", "r+") as file:
        for line in file:
            if host in line:
                break
        else:  # not found, we are at the eof
            file.write("{}\n".format(host))  # append missing datd
    file.close()


def update_hostname(inp):
    os.remove('single.txt')
    file = open("single.txt", "w")
    file.write(inp)
    file.write('\n')
    file.close()
