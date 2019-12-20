from xlwt import Workbook
import Brickuserlist.userslist1 as BKL
import Brickuserlist.permissionslist as BKP
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, "User Name")
sheet1.write(0, 1, "User Mail ID")
sheet1.write(0, 2, "User Created date")
sheet1.write(0, 3, "User Created Time")
sheet1.write(0, 4, "User last Login at date")
sheet1.write(0, 5, "User last Login at time")
sheet1.write(0, 6, "folder path and permissions levals")
for x in range(len(BKL.Lis)):
    per = []
    for y in range(len(BKP.PerLi)):
        if BKL.Lis[x]['id'] == BKP.PerLi[y]['user_id']:
            per.append(BKP.PerLi[y]['path'])
    sheet1.write(x+1, 6, '{}'.format(set(per)))


"""print("User ID : {}".format(Lis[4]['id']))
print("User Name : {}".format(Lis[4]['username']))
print("User Mail ID : {}".format(Lis[4]['email']))
print("User created_at : {}".format(Lis[4]['created_at']))
print("User last_login_at : {}".format(Lis[4]['last_login_at']))
print("password_set_at : {}".format(Lis[4]['password_set_at']))"""

for i in range(len(BKL.Lis)):
    sheet1.write(i+1, 0, '{}'.format(BKL.Lis[i]['username']))
    sheet1.write(i + 1, 1, '{}'.format(BKL.Lis[i]['email']))
#    sheet1.write(i + 1, 2, '{}'.format(BKL.Lis[i]['created_at'][:10]))
#   sheet1.write(i + 1, 3, '{}'.format(BKL.Lis[i]['created_at'][11:19]))
"""    if BKL.Lis[i]['last_login_at'] == 'null':
        sheet1.write(i + 1, 4, '{}'.format("Never"))
        sheet1.write(i + 1, 5, '{}'.format("Never"))
    else:
        sheet1.write(i + 1, 4, '{}'.format(BKL.Lis[i]['last_login_at'][:10]))
        sheet1.write(i + 1, 5, '{}'.format(BKL.Lis[i]['last_login_at'][11:19]))"""

"""print("User ID : {}".format(Lis[i]['id']))
    print("User Name : {}".format(Lis[i]['username']))
    print("User Mail ID : {}".format(Lis[i]['email']))
    print("User created_at : {}".format(Lis[i]['created_at']))
    print("User last_login_at : {}".format(Lis[i]['last_login_at']))
    print("password_set_at : {}".format(Lis[i]['password_set_at']))"""
wb.save('Brick_FTP_Users1.xls')
