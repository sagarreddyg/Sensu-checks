#API command to get list for users from Brick-FTP
#curl -u API_KEY:x https://YOUR_SUBDOMAIN.files.com/api/rest/v1/users.json
#for page 2 use below command
#curl -u API_KEY:x https://YOUR_SUBDOMAIN.files.com/api/rest/v1/users.json?page=2&per_page=1
import sys
import os

#API_KEY = sys.argv[1]

#CMD = "curl -u {}:x https://YOUR_SUBDOMAIN.files.com/api/rest/v1/users.json >> FTPuserlist.txt".format(API_KEY)
#CMD2 = "curl -u {}:x https://YOUR_SUBDOMAIN.files.com/api/rest/v1/users.json?page=2 >> userlist.json".format(API_KEY)
#os.system(CMD)
#os.system(CMD2)
