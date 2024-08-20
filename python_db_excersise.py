import mysql.connector
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
)
#creating a cursor:
mycr = mydb.cursor()
mycr.execute("USE oneteamsolutions")


def listing():
    a = int(input("enter the id of the employee:"))
    mycr.execute("SELECT * FROM emp_management where id = %s",(a,))
    result = mycr.fetchall()
    for i in result:
        print(i)
    
def add():
    id = int(input("enter the id of the employee:"))
    name = input("enter the name of the employee:")
    age = int(input("enter the age of the employee:"))
    salary = int(input("enter the salary of the employee:"))
    val = ("insert into emp_management values(%s,%s,%s,%s)")
    fields = (id,name,age,salary)
    mycr.execute(val,fields)
    mydb.commit()
    print("ADDED SUCCESSFULY")
    
def delete():
    id = int(input("enter the id of the employee:"))
    mycr.execute("DELETE FROM EMP_MANAGEMENT WHERE ID=%s",(id,))
    mydb.commit()
    print("DELETED SUCCESSFULLY")
    
def edit():
    id = int(input("enter the id of the employee:"))
    newname = input("enter the new name")
    newage = int(input("enter the new age:"))
    newsal = int(input("enter the salary:"))
    mycr.execute("Update emp_management set name=%s,age=%s,salary=%s where id=%s",(newname,newage,newsal,id))
    mydb.commit()
    print("Updated Succesfully")
    
while True:
    print("\n1. List")
    print("\n2. Add")
    print("\n3. Edit")
    print("\n4. Delete")
    print("\n5. Exit")
        
    choice = int(input("enter the choice:"))
        
    if choice == 1:
        listing()
    elif choice == 2:
        add()
    elif choice == 3:
        edit()
    elif choice == 4:
        delete()
    elif choice == 5:
       print("Exiting...")
       break
    else:
        print("Wrong choice.") 