import tkinter as tk
import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

def submitact():
	global U
	global P
	user = "root"
	passw = ""
	U=del_id_box.get()
	P=password.get()
	logintodb(user, passw)
	

def logintodb(user, passw):
	global U
	if passw:
		db = mysql.connector.connect(host ="localhost",user = user,password = passw,db ="courier_tracking")
		cursor = db.cursor()
	else:
		cursor = db.cursor()
	savequery = ""
	try:
		cursor.execute("select user.user_id, user_name,delivery.del_id,del_add,track_id,track_place,track_status from user join login on user.user_id = login.user_id join delivery on user.user_id=delivery.user_id join track on track.del_id=delivery.del_id where delivery.del_id="+str(U)+"&& login.user_pass='"+str(P)+"'")
		myresult = cursor.fetchone()
		db.commit()
		my_str.set(myresult)
		for x in myresult:
			print(x)
		print("Query Executed successfully")
		l1 = [r for r in myresult.keys()]
		print(U)
		print(P)
	except:
		db.rollback()
		print("Error occurred")


def delete():    
	global U
	global P
	user = "root"
	passw = ""
	U=del_id_box.get()
	P=password.get()
	if passw:
		db = mysql.connector.connect(host ="localhost",user = user,password = passw,db ="courier_tracking")
		cursor = db.cursor()
	else:
		cursor = db.cursor()
	savequery = ""
	
	try:
		cursor.execute("delete FROM payment WHERE del_id ="+str(U))
		cursor.execute("delete FROM track WHERE del_id = "+str(U))
		cursor.execute("delete FROM delivery WHERE del_id ="+str(U))
		db.commit()
		print("Query Executed successfully")
		myresult = cursor.fetchall()
		Output1 = "Cancelled successfully"
		Output1 += "\n Confirm Cancellation"
		Output1 += "\n Your Delivery ID:" + U
		messagebox.showinfo('Status', Output1)
		for x in myresult:
			print(x)
	except:
		db.rollback()
		print("Error occurred")

		

def insert():
        db=mysql.connector.connect(host="localhost",user="root",password="",db="courier_tracking")
        cursor = db.cursor()
        name=NAME.get()
        userid=USERID.get()
        username=USERNAME.get()
        userpass=PASSWORD.get()
        useradd=USERADD.get()
        try:
                cursor.execute("insert into user (user_id,user_name,user_add) values ("+str(userid)+","+"'"+str(name)+"'"+","+"'"+str(useradd)+"'"+")")
                cursor.execute("insert into login (user_id,username,user_pass) values ("+str(userid)+","+"'"+str(username)+"'"+","+"'"+str(userpass)+"'"+")")
                db.commit()
                print("REGISTRATION SUCCESSFUL")
                myresult=cursor.fetchall()
                Output = "Hello," + name
                Output += "\nTHANK YOU FOE REGISTERING, \nYOUR REGISTRATION WAS SUCCESSFUL"
                Output += "\n"
                Output += "\nRegistration Details:"
                Output += "\nNAME:" + name
                Output += "\nUSER NAME:" + username
                Output += "\nUSER PASSWORD:" + userpass
                Output += "\nUSER IDENTIFICATION:" + userid
                Output += "\nUSER ADDRESS:" + useradd
                messagebox.showinfo('Status',Output)
                for x in myresult:
                        print(x)
        except:
                db.rollback()
                print("Error occurred")



def update():
        user = "root"
        passw=""
        U=del_id_box.get()
        P=password.get()
        a=updateadd.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",db="courier_tracking")
        cursor = db.cursor()

        try:
                cursor.execute("UPDATE delivery set del_add='"+str(a)+"' where del_id="+str(U))
                db.commit()
                print("Address updated successfully,Click Fetch to know the Status")
                myresult=cursor.fetchall()

                Output = "Hello,"
                Output += "\nYOUR ADDRESS WAS UPDATED SUCCESSFULLY"
                Output += "\n"
                Output += "\nDELIVERY_ID:" + U
                Output += "\nUPDATED ADDRESS:" + a
                messagebox.showinfo('Status',Output)
                for x in myresult:
                        print(x)
        except:
                db.rollback()
                print("Error occurred")
                messagebox.showerror()



root = tk.Tk()
root.geometry("1900x1900")
root.iconbitmap("C://Users//pruth//OneDrive//Documents//PES//SEM V//DBMS//Lab//Project//truck.ico")
root.resizable(width=False,height=False)
root.title("PSP Couriers Pvt.Ltd")

Dataframe=Frame(root,bd=20,relief = RIDGE)
Dataframe.place(x=680, y=0, width=538, height = 200); 
img = ImageTk.PhotoImage(Image.open("C://Users//pruth//OneDrive//Documents//PES//SEM V//DBMS//Lab//Project//logo1.png"))
label = Label(root, image = img)
label.pack()


Dataframe=Frame(root,bd=20,relief = RIDGE)
Dataframe.place(x=0, y=200, width=1900, height = 390); 

wel = tk.Label(root, text = "WELCOME", font = ("arial",10,"bold"), fg = "RED")
wel.place(x = 920, y = 200)


del_id = tk.Label(root, text = "ENTER DELIVERY ID :", font = ("arial",20,"bold"), fg = "#9898F5")
del_id.place(x = 500, y = 250)

del_id_box = tk.Entry(root, width = 35)
del_id_box.place(x = 900, y = 250, width = 500, height = 35)



passw = tk.Label(root, text ="ENTER YOUR PASSWORD :", font = ("arial",20,"bold"), fg = "#9898F5")
passw.place(x = 500, y = 325)

password = tk.Entry(root, width = 35)
password.place(x = 900, y = 325, width = 500, height = 35)


fetchbtn = tk.Button(root, text = "FETCH",bg = "green",fg ="white",font=("arial",15,"bold"),command = submitact)
fetchbtn.place(x = 650, y = 375, width = 200)

delbtn = tk.Button(root, text ="CANCEL",bg = "green",fg ="white",font=("arial",15,"bold"),command = delete)
delbtn.place(x = 1050, y = 375, width = 200)


addupdate = tk.Label(root, text ="UPDATE ADDRESS :",font = ("arial",20,"bold"), fg = "#9898F5" )
addupdate.place(x = 500, y = 450)

updateadd = tk.Entry(root, width = 35)
updateadd.place(x = 790, y = 450, width = 620, height = 35)

updbtn = tk.Button(root, text ="UPDATE ADDRESS",bg = "green",fg ="white",font=("arial",15,"bold"),command = update)
updbtn.place(x = 850, y = 515, width = 200)



Dataframe=Frame(root,bd=20,relief = RIDGE)
Dataframe.place(x=0, y=600, width=650, height = 400);


head = tk.Label(root, text ="Register If New User:", font=("arial",15,"bold"), fg = "orange")
head.place(x = 30, y = 630)

head2 = tk.Label(root, text ="Status", font=("arial",15,"bold"), fg = "orange")
head2.place(x = 680, y = 630)

entername = tk.Label(root, text ="ENTER NAME:",font = ("arial",15,"bold"), fg = "#9898F5" )
entername.place(x = 30, y = 680)

NAME = tk.Entry(root, width = 100)
NAME.place(x = 350, y = 685, width = 200)


USER= tk.Label(root, text ="ENTER USER NAME:",font = ("arial",15,"bold"), fg = "#9898F5" )
USER.place(x = 30, y = 730)

USERNAME = tk.Entry(root, width = 100)
USERNAME.place(x = 350, y = 735, width = 200)


PASS= tk.Label(root, text ="ENTER USER PASSWORD:",font = ("arial",15,"bold"), fg = "#9898F5" )
PASS.place(x = 30, y = 780)

PASSWORD = tk.Entry(root, width = 100)
PASSWORD.place(x = 350, y = 785, width = 200)


USID= tk.Label(root, text ="ENTER USER IDENTIFICATION:",font = ("arial",15,"bold"), fg = "#9898F5" )
USID.place(x = 30, y = 830)

USERID = tk.Entry(root, width = 100)
USERID.place(x = 350, y = 835, width = 200)


US_ADD = tk.Label(root, text ="ENTER USER ADDRESS:",font = ("arial",15,"bold"), fg = "#9898F5" )
US_ADD.place(x = 30, y = 880)

USERADD = tk.Entry(root, width = 100)
USERADD.place(x = 350, y = 885, width = 200)


Dataframe=Frame(root,bd=20,relief = RIDGE)
Dataframe.place(x=650, y=600, width=1250, height = 400);

head2 = tk.Label(root, text ="Status:", font=("arial",15,"bold"), fg = "orange")
head2.place(x = 680, y = 630)


insbtn = tk.Button(root, text ="Create", bg = "green",fg ="white",font=("arial",15,"bold"),command = insert)
insbtn.place(x = 250, y = 920, width = 100)


style=ttk.Style()
style.theme_use('clam')

tree=ttk.Treeview(root, column=("C1","C2","C3","C4","C5","C6","C7"), show='headings', height=0)
tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
tree.heading("# 1", text="USER ID")
tree.column("# 2", anchor=CENTER, stretch=NO,width=100)
tree.heading("# 2", text="USER NAME")
tree.column("# 3", anchor=CENTER, stretch=NO, width=70)
tree.heading("# 3", text="DEL ID")
tree.column("# 4", anchor=CENTER, stretch=NO, width=275)
tree.heading("# 4", text="DELIVERY ADDRESS")
tree.column("# 5", anchor=CENTER, stretch=NO, width=80)
tree.heading("# 5", text="TRACK ID")
tree.column("# 6", anchor=CENTER, stretch=NO,width=100)
tree.heading("# 6", text="TRACK PLACE")
tree.column("# 7", anchor=CENTER, stretch=NO,width=100)
tree.heading("# 7", text="STRACK STATUS")

tree.place(x = 775, y = 632)

my_str = tk.StringVar()
l2 = tk.Label(root,textvariable=my_str, font = ("Times",20,"bold") ,fg='black' )   
l2.place(x = 780, y = 670)

#my_str.set("Output:")


root.mainloop()


