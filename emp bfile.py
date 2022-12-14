import pickle
l0=['Emp_ID','Emp_name']
file=open("employee.dat",'wb')
pickle.dump(l0,file)
l1=[1,'User1']
pickle.dump(l1,file)
l2=[2,'User2']
pickle.dump(l2,file)
file.close()

emp_id=1
emp_name="User1"
file=open("employee.dat",'rb')
while True:
    try:
        lst=pickle.load(file)
        if  emp_id==lst[0] and emp_name==lst[1]:
            print("done")
            break
    except EOFError:
        print("Invalid employee credential")
        exit()
file.close()
        
