import mysql.connector
class database:
    def __init__(self):    #its a constructor for creating object where self is an object
            self.con= mysql.connector.connect(
                host='localhost',
                user='root',
                password='Bu$#r@12',
                port='3306',
                database='py',
                auth_plugin='mysql_native_password'
            )
      #throguh this keyword  con we will find  the connection andthorug which we  will find queries
        #creating table through python program  : if not exist

            query='create table if not  exists user(userid int Primary key ,username varchar(200), phone varchar(12)) '

            #creating cursor for con varaible
            cursor = self.con.cursor()
            cursor.execute(query) #means table get created
            print(" table \"user \"created")
            #inserting value in table using methhod or function
    def create_table(self,tablename, columns):
        query='create table {} ( {})'.format(tablename,columns)
        cursor=self.con.cursor()
        cursor.execute(query)
        print(query)
        print("Table ",tablename," created !")

    def insert_user(self, table,  values,column=0):
        if column!=0:
            query = "insert into {}  ({})\
                 values({})".format(table, column, values)
        else:
            query = "insert into {}  \
                            values({})".format(table, values)

        print(query)

        cur2 = self.con.cursor()

        try:
            cur2.execute(query)
        except:
            print(f"{values} already exist! ")
        self.con.commit()
       # commit:physically changes in database
        print("user save to database")


    #fetching data

    def  fetch_all_data(self, table_name):
        query="select * from {}".format(table_name)
        cursor=self.con.cursor()
        cursor.execute(query)
        for row in cursor: #one row at a time from cusror
            print(row)


    def fetch_any_attribute(self,attribute,tablename): #fetching just an attribute(column) ||
        query="select {} from {}".format(attribute, tablename)
        cursor=self.con.cursor()
        cursor.execute(query)
        for a_row in cursor :
            print(any,": ",str(a_row))

    def fetch_any_record_data(self, tablename,attr,value): #fetching record of a particular person =
        query="select * from {} where {}={}".format(tablename, attr,value)
        cursor=self.con.cursor()
        try:
            cursor.execute(query)
            for row in cursor:
                print(row)
        except:
            print("No such attribute exist! ")
   #deleteing user from user table
    def delete_any_user(self,tablenamee, attr,value):
        query = "delete from {} where {}='{}\' ".format(tablenamee,attr,value)
        cursor = self.con.cursor()  #taking connection(con) from self(class object) and cursor  and storing it into varaible cusror
        try:
            cursor.execute(query)
        except:
            print(f'Attribute {attr} not exist ! ')
        # commit:physically changes in database
        self.con.commit()
        print(f'value {value} deleted from {attr} attribute sucesfully')
    #updating user in databasse
    def update_user(self, tablename, column_name, new_value_for_column,prikey,value):
       #as we can update column only with the help of primary key :userid is primary key

       query = "update {} SET {}='{}\' WHERE {}={}".format(tablename, column_name,new_value_for_column,prikey,value)
       cursor=self.con.cursor()
       cursor.execute(query)
       print(query)
       self.con.commit()
       print(query)
       print("Value updated ")
    def update_attribute_name(self, tablename, oldcolumn,newcolumn):
        query="ALTER TABLE {} RENAME  COLUMN {} TO {}".format(tablename,oldcolumn,newcolumn)
        cursor=self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(query)
        print(f'Attribute name :  {oldcolumn} updated to {newcolumn} succesfully!')
    def update_datatype_attribute(self, tablename, column, newdatatype):
        query="ALTER TABLE {} MODIFY  {} {}".format(tablename,column,newdatatype)
        cursor=self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print( query)
        print(f'DATA type of {column} updated to {newdatatype} seucesfully!')
    def add_constraint(self,tablename, constriant_type, *attributes):
        query="Alter table {} Add constraint {} ({} )".format(tablename,constriant_type,*attributes)
        cursor = self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f'Table  attribute constraint executed !')
    def update_tablename(self, tablename, newtable_name):
        query="ALTER TABLE {}  RENAME TO {}".format(tablename,newtable_name)
        cursor=self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f'Table name {tablename} changes to : {newtable_name}')
    def add_attributes(self, tablename , attribute, datatype=0):
        query="ALTER TABLE {} ADD {} {}".format(tablename, attribute,datatype)
        cursor=self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f' Attribute {attribute } Data type: {datatype} added sucesfully to table : {tablename} ')

    def set_default_name(self,tablename,attribute,default_name):
        query="Alter table {} ALTER {} Set DEFAULT \'{}\'".format(tablename,attribute,default_name)
        cursor = self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f' Default value set for {attribute}  default value: {default_name} ')
    def  drop_default(self,tablename,attribute):
        query="ALTER TABLE {}  ALTER {} DROP DEFAULT ".format(tablename,attribute)
        cursor=self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f'Default value drop for attribute:  {attribute} ')
    def check_constraint(self,tablename,check_name,condition):
        query="Alter table {}  ADD constraint {} check ({})".format(tablename,check_name,condition)
        cursor = self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        print(f' constraint {check_name} added sucesfully! ')
    def order_by(self,tablename,colmn ,desc=0):
        if desc!=0:
            query="Select * from {} order by  {} {} ".format(tablename,colmn,desc)
        else:
            query = "Select * from {} order by  {}  ".format(tablename, colmn)
        cursor = self.con.cursor()
        cursor.execute(query)
        for row in cursor:
            print(row)
  #self.functionname : to execute same member function in another member function of same class
    def count_row(self,tablename):
        query="SELECT COUNT(*) FROM  {}".format(tablename)
        cursor = self.con.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0] # storing total  records counting  in variable count
        print("Total rows : ",count)
    def count_attribute(self,tablename):
        query="SELECT COUNT(*) FROM information_schema.columns WHERE table_name= \'{}\'".format(tablename)
        cursor = self.con.cursor()
        self.con.commit()
        cursor.execute(query)
        count = cursor.fetchone()[0]  # storing total number of column in count
        print(f"Total  Attribute(column)  in table {tablename}= {count} ")
        return count
    def drop_table(self,tablename):
        query="drop table {} ".format(tablename)
        cursor=self.con.cursor()
        cursor.execute(query)
        print(f"Table {tablename} deleted permanently! ")
    def truncate_table(self,tablename):
        query="TRUNCATE TABLE {}".format(tablename)
        cursor = self.con.cursor()
        cursor.execute(query)
        print(f"Table {tablename} is empty now !   ")

obj=database()

#obj.insert_user('bushra' ,"id,name,age,state","7,'exo',21,'kanpur'\ ")
#obj.insert_user('bushra' ,"id,name,age,state","18,'xoxo',20,'max' ")
#obj.insert_user('bushra' ,"8,'heyy',20,'usa' ")

















