# Hospital-Management

My project on Hospital management system aims to develop the software that covers all the aspects of Management and operations of the Out-patient department. It aims to enable the hospital staff to improve operational effectiveness, reduce errors, time consumption and enhance delivery and quality of care. 
This project implements all activities of a hospital in a automated way using the python programming language to fasten the performance and also to make all the functions paperless and easy for both, the staff and the patients. 

A. SCOPE OF THE PROJECT:
•	Authentic login for the hospital staff
•	Add doctor records
•	Update doctor records
•	Delete doctor records
•	View list of doctors
•	Add patient records
•	Update patient records
•	Delete patient records
•	View list of patients
•	Book an online appointment with a doctor
•	View records of all the previous appointments
•	View graphical records of appointments

B. HARDWARE AND SOFTWARE REQUIREMENTS:

1.	HARDWARE:
A desktop computer (with a high resolution screen, comfortable keyboard and mouse and a moderately fast CPU)
Or a laptop (with a big screen, better resolution and a comfortable keyboard).

2.	SOFTWARE:
•	An operating system:  Python is a cross-platform language and works on Windows, macOS, and Linux. (For using Python 3.5 or above, Windows XP is not supported.)
•	Python: Download python from www.python.org .
•	Text editors and IDE such as jupyter or Visual studio IDE.

C. PYTHON MODULES USED:

1.	PICKLE MODULE:
Pickle module was used to create, update, and alter the various binary files used in this project such as emp.dat, doc.dat and patient.dat.

2.	OS MODULE:
OS module was used to update the binary files using the two file method that is, to remove and rename existing binary files.

3.	DATE-TIME MODULE:
Date-time module was used to deal with dates, times and time intervals in the login function, appointment function etc.

4.	MATPLOTLIB LIBRARY:
Matplotlib library was used to incorporate graphical representation of the data of previous appointments of various doctors.

D. IN-BUILT FUNCTIONS USED:
1. Open(): This function opens a file, and returns it as a file object. 
2. Close(): This function closes and open file. It's important to close an open file or else due buffering to a file may not show until we close the file.
3.	Int(): This function converts the specified value into an integer number. 
4.	Input(): This function allows the user to input some text or data for the specific variable. 
5.	Load(): This function of pickle module reads the pickled byte stream of one or more python objects from a file object. 
6.	Dump(): This function of pickle module serializes a python object and returns the bytes object. 
7.	Read(): Returns the read bytes in form of a string. Reads 'n' bytes, if no specified reads the entire file. 
8.	Write(): Inserts the string line in the text file. 
9.	Remove(): This function of OS module removes or deletes file path. 
10.	Rename(): This function of OS module renames a file.

E. USER-DEFINED FUNCTIONS:
I.	login(): The login function ensures authentication by allowing only those employees whose credentials are in the employee.dat file to be able to sign in. It also displays a record of the login date and time after login is done successfully. We have also used tkinter to make the login interface visually pleasing.
II.	 createfile():  This function accepts patient details from the user, creates a patient record and dumps it in the binary file patient.dat. 
III.	displayfile(): This function reads the patient records from the patient.dat file and prints them in the form of a table using formatted output.
IV.	deleterlist(): This function accepts the patient id of the record to be deleted from the user and then deletes that record from the patient file. It displays an ‘Invalid id’ message if the patient id does not already exist in the patient file.
V.	update_file(): This function accepts the patient id of the record to be updated from the user, provides 3 options of data to be changed (i.e., address, contact no., reason for consultation), accepts the new data from the user and modifies the data accordingly in the patient file. It displays an ‘Invalid id’ message if the patient id does not already exist in the patient file.
VI.	 create_lst(): This function reads the binary file doc.dat and then creates a list of records.
VII.	 print_doc(): This function prints doctor records in the form of a table using formatted output. The appointment schedule of doctors is also reflected in the doctor table.
VIII.	add_doc(): This function accepts doctor details from the user, auto generates the doctor id according to the department of the doctor, creates a new record and then dumps it in the binary file doc.dat. 
IX.	mod_doc(): This function accepts the doctor id of the doctor whose details are to be updated and the modified working days of that doctor from the user, makes the corresponding change in the doctor file and then prints the updated record of doctors. It displays an ‘Invalid id’ message if the doctor id does not already exist in the doctor file.
X.	del_doc(): This function accepts the doctor id of the doctor whose record is to be deleted from the user, deletes that record from the doctor file and then prints the updated record of doctors. . It displays an ‘Invalid id’ message if the doctor id does not already exist in the doctor file.
XI.	book_app(): This function enables the users to book an appointment with a doctor. It accepts the patient id and doctor id from the user, generates and returns the time at which the appointment has been booked to avoid any clash with other appointments. It displays an ‘Invalid’ message in case the patient id or doctor id are not already present in the respective files.
XII.	revise_app(): This function ensures that the previous appointments are not reflected in the doctor table and instead get stored in a text file named ‘app_record’. This function ensure that only the upcoming appointments are displayed when the print_doc() is used. 
XIII.	plotdrgraph(): This function uses matplotlib module to display a bar graph of the number of appointments versus the doctor id for each doctor to incorporate data visualisation.
XIV.	signout(): This function displays a signout interface using tkinter and exits from the program.

F. FILES CREATED:
1. Doctor binary file
2. Hospital employee binary file
