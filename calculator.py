from tkinter import*
from customtkinter import*
import mysql.connector

try:
    cnn = mysql.connector.connect(host='localhost', user='root', passwd='',database='calculator')
    cursor = cnn.cursor()

except mysql.connector.Error as e:
    excet=CTk()
    excet.title("Error")
    excet.geometry("300x100")
    cmsg=CTkLabel(excet,text=f"Error connecting to database: {e}")
    cmsg.place(x=20,y=20)
    cbtn=CTkButton(excet,text="OK",command=excet.destroy)
    cbtn.place(x=120,y=50)
    print(f"The error '{e}' occurred")


result = 0
sql=""

def add_numbers():
    global num1, num2,sql
    num1 = n1.get()
    num2 = n2.get()
    global result 
    result= int(num1) + int(num2)
    sql=(f"INSERT INTO adddb (n1, n2, result) VALUES('{num1}', '{num2}', '{result}');")

    
def sub_numbers():
    global num1, num2,sql
    num1 = n1.get()
    num2 = n2.get()
    global result 
    result= int(num1) - int(num2)
    sql=(f"INSERT INTO subdb (n1, n2, result) VALUES('{num1}', '{num2}', '{result}');")

    
def mul_numbers():
    global num1, num2 ,sql
    num1 = n1.get()
    num2 = n2.get()
    global result 
    result= int(num1) * int(num2)
    sql=(f"INSERT INTO muldb (n1, n2, result) VALUES('{num1}', '{num2}', '{result}');")

    
def div_numbers():
    global num1, num2,sql
    num1 = n1.get()
    num2 = n2.get()
    global result 
    result= float(num1) / float(num2)
    result=round(result,2)
    sql=(f"INSERT INTO divddb (n1, n2, result) VALUES('{num1}', '{num2}', '{result}');")

    

def see():
    global num1, num2, result,sql
    # sql=(f"INSERT INTO calculator (n1, n2, result) VALUES('{num1}', '{num2}', '{result}');")
    try:
        cursor.execute(sql)
        cnn.commit()
        ans.configure (text=result)
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")


def his_clear():
    try:
        cursor.execute("TRUNCATE TABLE adddb")
        cursor.execute("TRUNCATE TABLE subdb")
        cursor.execute("TRUNCATE TABLE muldb")
        cursor.execute("TRUNCATE TABLE divddb")
        cnn.commit()
        c=CTk()
        c.title("History Clear")
        c.geometry("300x100")
        cmsg=CTkLabel(c,text="History Cleared")
        cmsg.place(x=110,y=20)
        cbtn=CTkButton(c,text="OK",command=c.destroy)
        cbtn.place(x=80,y=50)
        c.mainloop()
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")


def see_history():
    try:
        global sql
        sql=(f"select * from adddb;")
        cursor.execute(sql)
        resadd = cursor.fetchall()
        cnn.commit()
        # print("add db")
        # print(resadd)
        # add = CTkLabel(r,text="r",width=5)
        # add.grid(row=0,column=0)
        # print("\n")
        sql=(f"select * from subdb;")
        cursor.execute(sql)
        ressub = cursor.fetchall()
        cnn.commit()
        # print("sub db\n")
        # print(ressub)
        # print("\n")
        sql=(f"select * from muldb;")
        cursor.execute(sql)
        resmul = cursor.fetchall()
        cnn.commit()
        # print("mul db\n")
        # print(resmul)
        # print("\n")
        sql=(f"select * from divddb;")
        cursor.execute(sql)
        resdiv = cursor.fetchall()
        cnn.commit()
        # print("div db\n")
        # print(resdiv)
        # print("\n")

        r=CTk()
        r.title("History")
        r.geometry("720x300")
        add = CTkLabel(r,text=resadd,width=5)
        nadd=CTkLabel(r,text="Addition (N1, N2, Result) : ")
        nadd.grid(row=0,column=0)
        add.grid(row=0,column=1)
        sub = CTkLabel(r,text=ressub,width=5)
        nsub= CTkLabel(r,text="Subtraction (N1, N2, Result) : ")
        nsub.grid(row=1,column=0)
        sub.grid(row=1,column=1)
        mul = CTkLabel(r,text=resmul,width=5)
        nmul= CTkLabel(r,text="Multiplication (N1, N2, Result) : ")
        nmul.grid(row=2,column=0)
        mul.grid(row=2,column=1)
        div = CTkLabel(r,text=resdiv,width=5)
        ndiv= CTkLabel(r,text="Division (N1, N2, Result) : ")
        ndiv.grid(row=3,column=0)
        div.grid(row=3,column=1)
        r.mainloop()
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")



w = CTk()
w.title("Calculator")
w.geometry("325x400")
num1 = CTkLabel(w, text="Enter first number")
num2 = CTkLabel(w, text="Enter second number")
num1.place(x=20,y=10)
num2.place(x=20,y=40)

n1 = CTkEntry(w)
n2 = CTkEntry(w)
n1.place(x=150, y=10)
n2.place(x=150, y=40)

plus = CTkButton(w,text=" + ")
plus.configure(command=add_numbers, height=1,width=3)
plus.place(x=20,y=80)
minus = CTkButton(w,text=" - ")
minus.configure(command=sub_numbers, height=1,width=3)
minus.place(x=60,y=80)
multi = CTkButton(w,text=" X ")
multi.configure(command=mul_numbers, height=1,width=3)
multi.place(x=20,y=120)
div = CTkButton(w,text=" ÷ ")
div.configure(command=div_numbers, height=1,width=3)
div.place(x=60,y=120)
equal = CTkButton(w,text=" = ")
equal.configure(command=see, height=50,width=30)
equal.place(x=150,y=80)
see_history = CTkButton(w,text=" History ",command=see_history, height=50,width=130)
# see_history.configure()
see_history.place(x=20,y=160)
clr_history = CTkButton(w,text=" Clear History ")
clr_history.configure(command=his_clear, height=50,width=130)
clr_history.place(x=175,y=160)

ans = CTkLabel(w,text=result,width=5)
ans.place(x=220,y=83)

# result_name = CTkLabel(w,text="ANS")
clos_btn=CTkButton(w,text="Close",command=w.destroy)
clos_btn.place(x=100,y=350)

w.mainloop()
cnn.close()


