fp = open("List.txt")
for i, line in enumerate(fp):
    if i == 109:
        print(line)
fp.close()
