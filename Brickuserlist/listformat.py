import os

fin = open("permissions.json", "rt")
fout = open("out.txt", "wt")
for line in fin:
    fout.write(line.replace('null', "'null'"))
fin.close()
fout.close()

fin = open("out.txt", "rt")
fout = open("out1.txt", "wt")
for line in fin:
    fout.write(line.replace('true', "'true'"))
fin.close()
fout.close()

fin = open("out1.txt", "rt")
fout = open("out2.txt", "wt")
for line in fin:
    fout.write(line.replace('false', "'false'"))
fin.close()
fout.close()
fin = open("out2.txt", "rt")
fout = open("permissions.txt", "wt")
for line in fin:
    fout.write(line.replace('][', ","))
fin.close()
fout.close()
fin = open("permissions.txt", "rt")
fout = open("permissionslist.py", "wt")
for line in fin:
    fout.write(line.replace('[', "PerLi = ["))
fin.close()
fout.close()
os.remove("out.txt")
os.remove("out1.txt")
os.remove("out2.txt")
os.remove("permissions.txt")