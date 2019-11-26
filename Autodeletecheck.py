import ListofHosts
totalhosts = ListofHosts.HOSTS
criticalhosts = ListofHosts.get_listof_criticalhosts()


def auto_delete_check():
    for l in range(len(totalhosts)):
        with open("Critical.txt", "r+") as file:
            for line in file:
                if totalhosts[l][0] in line:
                    break
            else:  # not found, we are at the eof
                print(totalhosts[l][0])
                  #os.system('sensuctl check delete SSL-check-{} --skip-confirm'.format(totalhosts[l][0]))# append missing datd
        file.close()
