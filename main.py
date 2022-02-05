#from filename import classname
from database import database
obj=database()
def table():
    tablename=input("Enter table name : ")
    return tablename

def main():
    while True:
        print("Welcome to easy database creator tool!")
        print("_______________********_______________")
        print("Press 1  to create Table : ")
        print("Press 2 to  insert values: ")
        print("press 3 to fetch all Data from user  : ")
        print("press 4  to fetch an attribute from table  : ")
        print("press 5  to fetch a record from table  : ")
        print("press 6  to delete any record : ")
        print("press 7 to update table : ")
        print("press 8 to update attribute name  : ")
        print("press 9 to update data type of attribute  : ")
        print("press 10 to add constraints to table  : ")
        print("press 11 to  update table name  : ")
        print("press 12  to add a new attribute to table  : ")
        print("press 13  to set a default name for an attribute  : ")
        print("press 14 to Drop default  : ")
        print("press 15 to add check constraint: ")
        print("press 16 to sort table by a speecific column: ")
        print("press 17 to count number of records in table  : ")
        print("press 18 to count number of column in table  : ")
        print("press 19 to drop table : ")
        print("press 20 to truncate table : ")
        print("Enter 0 to exit: ")
        print()
        try:
            choice=int(input("enter Value:  "))
        except:
            print("Invalid input: ")
        match choice:
            case 1:
                tablename=table()
                columns=input("Enter columns of table along with its datatype  '\comma separted '\ format: name varchar(200): ")
                obj.create_table(tablename,columns)
            case 2:
                tablename=table()
                column=input("Enter  column name (comma separted): \n Note : if yu dont wanna fetch by  column so enter 0 :")
                values=input("Enter values specfic to their position (comma separted) : ")
                obj.insert_user('tablename','values','column')
            case 3:
                tablename=table()
                obj.fetch_all_data(tablename)
            case 4:
                tablename = table()
                column=input("Enter the attribute name  for fetching values : ")
                obj.fetch_any_attribute(column,tablename)
            case 5:
                tablename=table()
                attribute=input("Enter the Attribute  name : ")
                value=input("enter the value for given attribute ")
                obj.fetch_any_record_data(tablename,attribute,value)
            case 6:
                tablename=table()
                attribute = input("Enter the Attribute  name : ")
                value = input("enter the value for given attribute ")
                obj.delete_any_user(tablename,attribute,value)
            case 7:
                tablename=table()
                column_name=input("Enter column name of which you want to  update value: ")
                new_value=input("Enter new value to  set  for given column: ")
                prikey=input("Enter primary key name: ")
                value=input("Enter value for primary key: ")

                obj.update_user(tablename,column_name,new_value,prikey,value)
            case 8:
                tablename=table()
                oldcolumn=input("Enter exising attribute name  for re-naming :")
                new_column=input("Enter new name for given attribute: ")
                obj.update_attribute_name(tablename,oldcolumn,new_column)
            case 9:
                tablename=table()
                column=input("Enter name of column for updating data type: ")
                newdatatype=input("Enter new data type for column enteted : ")
                obj.update_datatype_attribute(tablename,column,newdatatype)
            case 10:
                tablename=table()
                const_type=input("Enter Constraint type : ")
                attribute=input("Enter attribute name for updating constraints: ")
                obj.add_constraint(tablename,const_type,attribute)
            case 11:
                tablename=table()
                new_name=input("Enter new name for table : ")
                obj.update_tablename(tablename,new_name)
            case 12:
                tablename = table()
                attr=input("Enter new attribute name to add : ")
                datatype=input("Enter data type for entered attribute in format datatype(range): ")
                obj.add_attributes(tablename,attr,datatype)
            case 13:
                 tablename=table()
                 attr = input("Enter attribute name to set default value: ")
                 def_name=input("Enter default name : ")
                 obj.set_default_name(tablename,attr,def_name)
            case 14:
                 tablename=table()
                 attr=input("Enter attriibute name to drop default: ")
                 obj.drop_default(tablename,attr)
            case 15:
                tablename=table()
                checkname=input("Enter the name you would like to give to check constraint:  ")
                condition=input("Enter the condition:  ")
                obj.check_constraint(tablename,checkname,condition)
            case 16:

                tablename = table()
                column=input("Enter the column name yto sort ")
                Desc=input("Enter 0 for ascending : and type desc for descending ")
                obj.order_by(tablename,column,Desc)
            case 17:
                tablename=table()
                obj.count_row(tablename)
            case 18:
                tablename=table()
                obj.count_attribute(tablename)
            case 19:
                tablename=table()
                obj.drop_table(tablename)
            case 20:
                tablename=table()
                obj.truncate_table(tablename)
            case 0:
                exit()
            case  _:
                print("Unexpeccted input! ")








if __name__=="__main__":
    main()



