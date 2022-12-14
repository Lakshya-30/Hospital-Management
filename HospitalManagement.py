print("Welcome to the Out Patient Department of the ABC hospital")
import pickle
from datetime import date,timedelta
import os
import time
from tkinter import *
#--------------------------------------LOGIN----------------------------------------------
def login():
    global emp_lst
    window=Tk()
    window.title("EMPLOYEE LOGIN")
    Label(window,text="Welcome to ABC hospital",bg="pink",width="300",height="2",font=("Palatino linotype",13)).pack()
    Label(text=" ").pack()
    Label(window,text="Enter your details",bg="light blue",width="300",height="2",font=("Calibri",13)).pack()
    empname=StringVar()
    empid=StringVar()
    empname_label=Label(window,text="EMPLOYEE NAME")
    empname_label.pack()
    empname_entry=Entry(window,textvariable=empname)
    empname_entry.pack()
    empid_label=Label(window,text="EMPLOYEE ID")
    empid_label.pack()
    empid_entry=Entry(window,textvariable=empid)
    empid_entry.pack()
    Label(text=" ").pack()
    Button(text="Login!",height="2",width="30",command=window.destroy).pack()
    window.mainloop()
    emp_lst=[]

    file=open("employee.dat",'rb')
    emp_name=empname.get()
    emp_id=empid.get()
    d=(date.today()).strftime('%d/%m/%y')
    t=time.strftime("%H:%M:%S")
    while True:
        try:
            lst=pickle.load(file)
            if int(emp_id)==lst[0] and emp_name==lst[1]:
                emp_lst.append([emp_name,emp_id,d,t])
                break
        except EOFError:
            print("Invalid employee credential")
            exit()
    file.close()
login()
def show():
    global emp_lst
    gap=' '*7
    print('='*120)
    heading=f"{'Employee name':15s}{gap}{'Employee id':<15s}{gap}{'Date':<10s}{gap}{'Time':<10s}"
    print(heading)
    print('='*120)
    l=[]
    for data in emp_lst:
        rec=f"{data[0]:15s}{gap}{data[1]:<5s}{gap}{data[2]:<10}{gap}{data[3]:<10}"
        print(rec)
    print('-'*120)
show()
    
#----------------------------TO CREATE PATIENT FILE---------------------------------------
def createfile():
    txtf=open("pid_record.txt",'a')
    pat_lst=[]
    pat_name=input("Enter patient name: ")
    pat_id=int(input("Enter patient id: "))
    pat_age=int(input("Enter patient age: "))
    pat_gender=input("Enter gender M/F: ")
    contact=int(input("Enter mobile number: "))
    address=str(input("Enter patient address: "))
    reason=str(input("Enter the reason for consultation: "))
    pat_lst.append([pat_name,pat_id,pat_age,pat_gender,contact,address,reason])
    with open('patient.dat','ab') as f:
        for rec in pat_lst:
            pickle.dump(rec,f)

#------------------------------TO DISPLAY PATIENT RECORDS---------------------------------      
def displayfile():
    gap=' '*7     #seven gap spaces between the columns
    heading=f"{'patient name':^20s}{gap}{'ID':<5s}{gap}{'age':<3s}{gap}{'gender':1s}{gap}{'contact':<10s}{gap}{'address':<20s}{gap}{'reason':<15s}"
    print('='*130)
    print(heading)
    print('-'*130)
    l=[]
    with open('patient.dat','rb') as f:
        while True:
            try:
                lst=pickle.load(f)
                l.append(lst)
            except EOFError:
                break
        for data in l[0:]:
            rec=f"{data[0]:20s}{gap}{data[1]:<5d}{gap}{data[2]:3d}{gap}{data[3]:1s}{gap}{data[4]:10d}{gap}{data[5]:20s}{gap}{data[6]:15s}"
            print(rec)
        print('='*130)

#--------------------------------TO DELETE PATIENT RECORDS--------------------------------
def deleterlist():
    import pickle
    lst1=[]
    with open ('patient.dat','rb') as f:
        while True:
            try:
                lst=pickle.load(f)
                lst1.append(lst)
            except EOFError:
                break
    #print(lst1)
    l=len(lst1)
    pat_id=int(input("Enter id of the patient whose records are to be deleted: "))
    for i in range(l):
        if lst1[i][1]==pat_id:
            p=lst1.pop(i)
            print("Deleted patient: ",p)
            break
    else:
        print("Invalid patient id...")
            
    with open ("patient.dat","wb") as f:
        for rec in lst1:
            pickle.dump(rec,f)

#----------------------------------TO UPDATE PATIENT RECORD-------------------------------
def update_file():
    pat_id=input("Enter patient id for updation: ")
    fin=open('patient.dat','rb')
    fout=open('temp.dat','wb')
    flag=1
    data=[]
    while True:
        try:
            rec=pickle.load(fin)
            while pat_id==str(rec[1]):
                flag=0
                x=input("Enter the name of the detail you want to update; options are contact,address,reason: ")
                if x=='contact':
                    contact=int(input("Enter new contact number: "))
                    rec[4]=contact
                elif x=='address':
                    address=input("Enter new address: ")
                    rec[5]=address
                else:
                    reason=input("Enter the changed reason for consultation: ")
                    rec[6]=reason
                print("Modified data is: ")
                break
            data.append(rec)
        except EOFError:
            if flag==1:
                print("Invalid id")
            break
    for rec in data:
        pickle.dump(rec,fout)
    fin.close()
    fout.close()
    os.remove('patient.dat')
    os.rename('temp.dat','patient.dat')
    displayfile()

#---------------------------------------SIGNOUT-------------------------------------------
def signout():
    root=Tk()
    root.title("SIGN OUT")
    Label(root,text="Click on ok and you will be signed out...",bg="violet",width="100",height="2",font=("Calibri",16)).pack()
    Label(text=" ").pack()
    Button(text="OK!!!",height="2",width="30",bg="light green",command=root.destroy).pack()
    root.mainloop()
    #break


from datetime import datetime
dlist=['immunology','cardiology','endocrinology','general medicine','neurology','gynaecology','pediatrics','psychiatry','rheumatology']

#----------------------------------TO CREATE DOCTOR LIST----------------------------------
def create_lst():
    file=open("doc.dat",'rb')
    lst1=[]
    while True:
        try:
            lst=pickle.load(file)
            lst1.append(lst)
        except EOFError:
            break
    file.close()
    return lst1 #lst1 created

#----------------------------------TO PRINT DOCTOR TABLE ---------------------------------
def print_doc(lst1):
    gap=" "*2
    heading=f"{'Doc_id':6s}{gap}{'Name':^15s}{gap}{'Department':<16s}{gap}{'Days available':^26s}{gap}{'Appointments{Pat.id:timings}':<}"
    print('='*125)
    print(heading)
    print('-'*125)
    for data in lst1[1:]:
        rec=f"{data[0]:6d}{gap}{data[1]:15s}{gap}{data[2]:16s}{gap}{data[3]:26s}{gap}{data[4]:}"
        print(rec)
    print('-'*125)

#------------------------------TO APPEND A DOCTOR RECORD----------------------------------
def add_doc():
    global dlist
    f=open("doc.dat",'ab')
    n=input("Enter name of employee:")
    d=input("Enter any 1 of 9 departments:").lower()
    l=create_lst()
    if d in dlist:
        for data in l[1:]:
            if data[2].lower()==d:
                Id=data[0]+1
        days=input("Enter working days:")
        l1=[Id,n,d.title(),days,{}]
        pickle.dump(l1,f)
        f.close()
        print("Record added")
        l=create_lst()
        print_doc(l)
    else:
        print("Department name is invalid")

#--------------------------------TO UPDATE WORKING DAYS-----------------------------------
def mod_doc():
    fin=open("doc.dat",'rb')
    fout=open('temp.dat','wb')
    rec=[]
    flag=1
    Id=int(input("Enter Doc_id for updation:"))
    while True:
        try:
            data=pickle.load(fin)
            if data[0]==Id:
                flag=0
                print('Name:',data[1])
                data[3]=input('Updated working days:')
            rec.append(data)
        except EOFError:
            if flag==1:
                print("Doc_id is not valid. Refer list of doctors")
            break
    for data in rec:
        pickle.dump(data,fout)
    fin.close()
    fout.close()
    os.remove("doc.dat")
    os.rename('temp.dat','doc.dat')
    l=create_lst()
    print_doc(l)

#--------------------------------TO DELETE DOCTOR RECORD----------------------------------
def del_doc():
    lst=create_lst()
    l=len(lst)
    Id=int(input("Enter Doc_id for deleting the record:"))
    for j in range(l):
        if lst[j][0]==Id:
             e=lst.pop(j)
             break
    else:
         print("Doc_id is not valid. Refer list of doctors")
    with open("doc.dat",'wb')as f:
        for rec in lst:
            pickle.dump(rec,f)
    print_doc(lst)

#----------------------------------BOOKING AN APPOINTMENT---------------------------------
def book_app():
    today=date.today()
    now=datetime.now()
    dayname=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dayno=today.weekday()
    fin=open("doc.dat",'rb')
    fout=open('temp.dat','wb')
    rec=[]
    flag=1
    f=open('patient.dat','rb')
    x=[]
    while True:
        try:
            data=pickle.load(f)
            x.append(data[1])
        except EOFError:
            break
    f.close()
    pat_id=int(input("Enter patient id:"))
    if pat_id in x:
        l=create_lst()
        print_doc(l)
        n=input("Enter doctor id:")
        while True:
            try:
                data=pickle.load(fin)
                if str(data[0])==n:
                    flag=0
                    if dayname[dayno] in data[3]:
                        t=now+timedelta(minutes=5)
                        time=t.strftime('%H:%M')
                        for i in data[4].values():
                            p=(datetime.strptime(i,'%H:%M')+timedelta(minutes=30)).strftime('%H:%M')
                            if t.strftime('%H:%M')<p :
                                time=p
                            else:
                                time=t.strftime('%H:%M')
                        if time>'20:00' or time<'09:00':
                            print('''The hospital opens at 09:00 AM and closes at 20:00 PM from Monday to Saturday.
Please try later.''')
                        else:
                            print('Appointment booked for',time,'hours with',n)
                            data[4][pat_id]=time
                        print('Thank you for choosing ABC hospitals')   
                    else:
                        print('''Doctor is not available today. Please refer list of doctors.''')
                rec.append(data)
            except EOFError:
                if flag==1:
                    print('Doctor id is not valid. Refer list of doctors.')
                break
        for data in rec:
            pickle.dump(data,fout)
        fin.close()
        fout.close()
        os.remove("doc.dat")
        os.rename('temp.dat','doc.dat')
    else:
        print('Patient id is invalid.')

#-------------TO REMOVE PREVIOUS APPOINTMENTS AND STORE THEM IN A TXT FILE----------------
def revise_app():
    fin=open("doc.dat",'rb+')
    fout=open('temp.dat','wb')
    rec=[]
    now=datetime.now()
    t=now.strftime('%Y/%m/%d')
    ftxt=open("app_record.txt",'a')
    while True:
        try:
            lst=pickle.load(fin)
            try:
                d=lst[4]
                for i in list(d):
                    if d[i] < (datetime.now()).strftime('%H:%M'):
                        rem=d.pop(i)
                        str1='\n'+str(t)+'->'+str(lst[0])+':'+str(i)+'-'+str(rem)
                        ftxt.write(str1)
            except TypeError:
                l1=lst
            rec.append(lst)
        except EOFError:
            break
    for data in rec:
        pickle.dump(data,fout)
    fin.close()
    fout.close()
    os.remove("doc.dat")
    os.rename('temp.dat','doc.dat')
    ftxt.close()

#--------------------------------------GRAPH----------------------------------------------
import matplotlib.pyplot as pl
def plotdrgraph():
    with open("app_record.txt",'r') as f:
        x=[]
        y=[]
        d=f.readlines()
        l=create_lst()
        for i in range(1,len(l)):
            count=0
            x.append(str(l[i][0]))
            for j in d:
                if int(j[12:15])==l[i][0]:
                    count+=1
            y.append(count)
    #print(x,y)
    pl.bar(x,y,color='g')
    pl.title("Record of appointments")
    pl.xlabel("Doc_id")
    pl.ylabel("Number of appointments")
    pl.show()
    
#-------------------------------------- MENU----------------------------------------------
ch='Y'
print('Welcome to ABC hospital.')
while ch.lower()=='y':
    print('''
1. Enter patient record
2. View list of patients
3. Update patient records
4. Delete patient record
5. View list of doctors
6. Add record of doctor
7. Update working days of an existing doctor
8. Delete record of a doctor
9. Book an appointment with a doctor
10. View graphical record of appointments
11. Sign out''')
    num=input("Which option do you want(1-11)? ")
    if num=='1':
        createfile()
    elif num=='2':
        displayfile()
    elif num=='3':
        update_file()
    elif num=='4':
        deleterlist()
    elif num=='5':
        revise_app()
        l=create_lst()
        print_doc(l)
    elif num=='6':
        add_doc()
    elif num=='7':
        mod_doc()
    elif num=='8':
        del_doc()
    elif num=='9':
        book_app()
    elif num=='10':
        plotdrgraph()
    elif num=='11':
        signout()
        exit()
    else:
        print("Option number is invalid.")
    ch=input("Do you want to continue(Y/N)?")
