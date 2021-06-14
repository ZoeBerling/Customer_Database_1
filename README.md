# Customer_Database_1
A project to organize the data from a customer form

A quick explanation of the files I uploaded 
1) Cx_InsertsDOA.py has all the SQL stored queries
2) Insert.py is where data can be inserted from the sampleinsert.csv- eventually this will be an API, but I decided to build out a class file to make this step easier (at the moment the itemclass.py is not connected since everything is imported as a list, but I think when I connect to the webform API it will force me to pull everything in field by field, so the class file will be more useful then)
3) sampleinsert.csv has some sample data
4) DisplayCXInserts is my very early-stage attempt to make a GUI for these tables- right now all it has is a tkinter button that downloads a csv of an SQL query that will likely be added as a procedure. 
5) itemclass.py : again, just some classes for my tables that aren't used for anything at the moment.
