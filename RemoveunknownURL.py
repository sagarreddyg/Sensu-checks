
def findunknownurl(urlnum):
    fp = open("List.txt")
    for i, line in enumerate(fp):
        if i == urlnum:
            return line
    fp.close()



def removeunknownurl(urlname):
    with open("List.txt", "r") as f:
        lines = f.readlines()
    with open("List.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != urlname:
                f.write(line)

def readknownurl(urlnum):
    fp = open("List.txt")
    for i, line in enumerate(fp):
        if i == urlnum:
            with open('Unknownurl.txt', 'a+') as fh:
                fh.write(line)
            fh.close()
    fp.close()
