import pickle
l0=['Doc_id','Name','Department','Days available','Appointments']
file=open("doc.dat","wb")
pickle.dump(l0,file)
l1=[101,'Dr. Arjun','Immunology',"Monday,Thursday",{}]
pickle.dump(l1,file)
l2=[201,'Dr. Kiran','Cardiology',"Monday,Thursday",{}]
pickle.dump(l2,file)
l3=[301,'Dr. Sudha','Endocrinology',"Tuesday,Wednesday",{}]
pickle.dump(l3,file)
l4=[401,'Dr. Harsh','General medicine',"Wednesday,Saturday",{}]
pickle.dump(l4,file)
l5=[402,'Dr. Aakash','General medicine',"Thursday,Friday",{}]
pickle.dump(l5,file)
l6=[501,'Dr. John','Neurology',"Monday,Wednesday",{}]
pickle.dump(l6,file)
l7=[601,'Dr. Mamta','Gynaecology',"Tuesday,Friday,Saturday",{}]
pickle.dump(l7,file)
l8=[701,'Dr. Chitra','Pediatrics',"Thursday,Saturday",{}]
pickle.dump(l8,file)
l9=[801,'Dr. Ravi','Psychiatry',"Wednesday,Friday",{}]
pickle.dump(l9,file)
l10=[901,'Dr. Sharan','Rheumatology',"Tuesday,Thursday",{}]
pickle.dump(l10,file)
file.close()



