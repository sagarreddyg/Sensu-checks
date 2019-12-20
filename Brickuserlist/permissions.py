# To get total permissions of users in page 1 from Brick FTP use belou command
#curl -u API_KEY:x https://app.files.com/api/rest/v1/permissions.json -H 'Content-Type: application/json'
#for page 2 use below command
#curl -u API_KEY:x https://app.files.com/api/rest/v1/permissions.json?page=2&per_page=1 -H 'Content-Type: application/json' -d '{"group_id":1,"user_id":1,"include_groups":true}'
import sys
import os

#API_KEY = sys.argv[1]

#CMD = "curl -u {}:x https://app.files.com/api/rest/v1/permissions.json > permissions.json".format(API_KEY)
#CMD2 = "curl -u {}:x https://app.files.com/api/rest/v1/permissions.json?page=2 >> permissions.json".format(API_KEY)
#os.system(CMD)
#os.system(CMD2)

