#   Part of the DCM GUI to control login for up to 10 different users
#   Author: Serena Santos (Group 3)
#   Date: September 2024
#
#   Function list:
#       - __init__(self): constructor
#       - startup(self): returns 1 if startup is successful and 0 otherwise
#       - shutdown(self): returns 1 once complete
#       - signup(self, username, password): returns 1 if signup is successful, 
#           0 if there are 10 users, and 2 if the username is taken
#       - login(self, username, password): returns 1 if login is successful and 0 if unsuccessful 
#       - delete(self, username, password): returns 1 if deletion is successful, 0 if unsuccessful 
#       - initialize_user_count(self): count number of users registered; returns number of users 
#       - clear_table(self): clears table of all contents
#       - print_table(self): displays entire table

#Using SQLite library for database
import sqlite3

class database:
    max_Users = 10
    user_count = 0
    #Create connection to database and cursor
    connection = sqlite3.connect("pacemaker.db")
    cursor = (connection).cursor()

    def __init__(self):
       print("ENTERING CONSTRUCTOR")

    #----------------------------startup()-----------------------------------------------------
    def startup(self):
        print("ENTERING STARTUP\n")
        
        #Create table for usernames and passwords; note num is the entry number (i.e. 5th login)
        (self.cursor).execute("CREATE TABLE IF NOT EXISTS loginInfo(username,password,num)")

        #Check if table has been created 
        # **sqlite_master should hold loginInfo
        check = (self.cursor).execute("SELECT name FROM sqlite_master WHERE name='loginInfo'")
        if (check.fetchone() == None):
            print("Table not found")
            return 0
        else:
            self.initialize_user_count()
            return 1

    #----------------------------shutdown()-----------------------------------------------------
    def shutdown(self):
        print("ENTERING SHUTDOWN\n")
        (self.connection).close()
        return 1

    #----------------------------signup()-----------------------------------------------------
    def signup(self, username, password):
        print("ENTERING SIGN UP\n")

        #Check if new user has been created (number of users is correct)
        if(self.user_count >= self.max_Users):
            return 0
        
        #Check if username is taken
        for row in (self.cursor).execute("SELECT username,password,num FROM loginInfo"):
            if (row[0] == username and row[1] == password): #change so that passwords dont matter
                return 2
        
        #Insert valid data into loginInfo table & commit changes to database
        row = [username, password, self.user_count]
        (self.cursor).execute("INSERT INTO loginInfo VALUES(?, ?, ?)", row)
        (self.connection).commit()
        self.user_count += 1
        
        return 1

    #----------------------------login()-----------------------------------------------------
    def login(self, username, password):
        print("ENTERING LOGIN\n")

        #go through each row in table and compare the username & passwords
        for row in (self.cursor).execute("SELECT username,password,num FROM loginInfo"):
            if (row[0] == username and row[1] == password):
                return 1
        
        return 0

    #----------------------------delete()-----------------------------------------------------
    def delete(self, username, password):
        print("ENTERING DELETE")

        found = 0
        #go through each row in table and compare the username & passwords
        for row in (self.cursor).execute("SELECT username,password,num FROM loginInfo"):
            if (row[0] == username and row[1] == password):
                found = 1

        if (found):
            delete_stm = 'DELETE FROM loginInfo WHERE username=?'
            (self.cursor).execute(delete_stm, (username,))
            (self.connection).commit()
            self.user_count -= 1
            return 1
        
        return 0

    #----------------------------initialize_user_count()-----------------------------------------------------
    def initialize_user_count(self):
        
        for row in (self.cursor).execute("SELECT num FROM loginInfo"):
            self.user_count += 1

    #----------------------------clear_table()-----------------------------------------------------
    def clear_table(self):
        print("ENTERING CLEAR TABLE")

        #go through each row in table and compare delete
        delete_stm = 'DELETE FROM loginInfo'
        (self.cursor).execute(delete_stm)
        (self.connection).commit()
        self.user_count = 0
            

    #----------------------------print_table()-----------------------------------------------------
    def print_table(self):
        print("------------------------------------")
        print("Users: (username, password, number)\n")
        for row in (self.cursor).execute("SELECT username,password,num FROM loginInfo"):
            print(row)
        print("\n------------------------------------\n")

    

