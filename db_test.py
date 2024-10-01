import database

#run tests on database class
db = database.database()

#---------Startup---------------
success = db.startup()
if (success):
    print("Test Passed: Startup Successful\n")
else:
    print("Test Failed: Startup unsuccessful\n")

db.print_table()

#---------Signup---------------
new_user = ["serena", "12345"]
success = db.signup(new_user[0], new_user[1])
if (success):
    print("Test Passed: Signup Successful\n")
else:
    print("Test Failed: Signup unsuccessful\n")

db.print_table()

#taken username test
success = db.signup(new_user[0], new_user[1])
if (success == 1):
    print("Test Failed: Signup Successful\n")
elif (success == 2):
    print("Test Passed: Username taken\n")
else:
    print("Test Failed: Wrong message\n")

db.print_table()

#exceeding 10 users test
for i in range(0,10):
    db.signup(chr(ord('a') + i), "1")

db.print_table()

success = db.signup("test", "2")
if (success == 1):
    print("Test Failed: Signup Successful\n")
elif (success == 0):
    print("Test Passed: Too many users registered\n")
else:
    print("Test Failed: Wrong message\n")


#---------Login---------------
success = db.login(new_user[0], new_user[1])
if (success):
    print("Test Passed: Login Successful\n")
else:
    print("Test Failed: Login unsuccessful\n")

success = db.login("bob", "12345")
if (success):
    print("Test Failed: Login Successful\n")
else:
    print("Test Passed: Login unsuccessful\n")


#---------Delete---------------
success = db.delete(new_user[0], new_user[1])
if (success):
    print("Test Passed: Deletion Successful\n")
else:
    print("Test Failed: Deletion unsuccessful\n")

#element not in table test
success = db.delete("hello", "123")
if (success):
    print("Test Failed: Deletion Successful\n")
else:
    print("Test Passed: Deletion unsuccessful\n")

db.print_table()
print("CLEARING TABLE")
db.clear_table()
db.print_table()

#no entries test
success = db.delete(new_user[0], new_user[1])
if (success):
    print("Test Failed: Deletion Successful\n")
else:
    print("Test Passed: Deletion unsuccessful\n")


#---------Shutdown---------------
success = db.shutdown()
if (success):
    print("Test Passed: Shutdown Successful\n")
else:
    print("Test Failed: Shutdown unsuccessful\n")

