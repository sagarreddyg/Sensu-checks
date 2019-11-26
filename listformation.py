import ListofHosts

cri = ListofHosts.get_listof_criticalhosts()
HOSTS = []
for i in range(len(cri)):
    HOSTS.append((cri[i], 443))
print(HOSTS)