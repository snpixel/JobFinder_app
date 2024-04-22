#before running the program run database file in mysql
#modules required
from tkinter import *
import mysql.connector as sqlcon

#to setup connection between database
mycon = sqlcon.connect(host="localhost",user="{your username}",passwd="{your password}",database="project")

cursor = mycon.cursor()

#to get user details
def user_entry():
    #to create a new window
    userEntry = Tk()
    userEntry.geometry('1000x720')
    
    #to know field
    def field_insert(field):
        global field_type
        field_type = field
        
    #to create input columns 
    name = Entry(userEntry, width=50, borderwidth=3)
    phoneNo = Entry(userEntry, width=50, borderwidth=3)
    experience = Entry(userEntry, width=50, borderwidth=3)
    
    #to add field buttons
    IT_button = Button(userEntry, text="IT", borderwidth=3,command=lambda: field_insert("IT") )
    Design_button = Button(userEntry, text="Design", borderwidth=3, command=lambda: field_insert("Design"))
    Managment_button = Button(userEntry, text="Managment", borderwidth=3,command=lambda: field_insert("Management"))

    #to insert the values in table
    def entry():
        cursor.execute("insert into user_info values('%s',%s,%s,'%s','%s')"%(name.get(),phoneNo.get(),experience.get(),field_type,username))
        mycon.commit()
        userEntry.destroy()
        user_data()
        
    #to add heading
    title_field = Label(userEntry, text="Select Field")

    #to position the buttons and title
    title_field.place(relx=0.4, rely=0.57,
                      anchor="center", height=50, width=75)
    IT_button.place(relx=0.4, rely=0.63, anchor="center", height=50, width=75)
    Design_button.place(relx=0.5, rely=0.63,
                        anchor="center", height=50, width=75)
    Managment_button.place(
        relx=0.6, rely=0.63, anchor="center", height=50, width=75)

    #to create button
    submit = Button(userEntry, text="Submit", command=entry, borderwidth=3)
    
    #to insert the blank entries
    name.insert(0,"enter your name")
    phoneNo.insert(0,"enter your phone number")
    experience.insert(0,"enter experience in years")
    
    #to place the input fiels and other things
    name.place(relx = 0.5 ,rely = 0.3 , anchor="center",height = 50)
    phoneNo.place(relx=0.5, rely=0.4, anchor="center", height=50)
    experience.place(relx=0.5, rely=0.5, anchor="center", height=50)
    submit.place(relx = 0.5 , rely = 0.7 , anchor="center" , height = 40 , width = 75)
    
    userEntry.mainloop()
#to manage data of admin
def admin_data():
    admin = Tk()
    admin.geometry("920x720")
    
    #to get tables
    def field_type(field):
        def remove_field_data(subfield):
            def submit1():
                cursor.execute("delete from %s where company = '%s' and subfield = '%s'" % (
                    field_for_fun, company.get(), subfield.get()))
                mycon.commit()
                enter.destroy()
                admin1.destroy()
                table_window(field_for_fun)

            enter = Tk()
            enter.geometry("920x720")
            
            #entry fields
            company = Entry(enter, width=50, borderwidth=3)
            subfield = Entry(enter, width=50, borderwidth=3)
            
            #button to execute the entry
            submit = Button(enter, text="Submit",
                            command=submit1, borderwidth=3)

            company.insert(0, "enter company name")
            subfield.insert(0, "enter Job")
            
            #to place the input fiels and other things
            company.place(relx=0.5, rely=0.2, anchor="center", height=50)
            subfield.place(relx=0.5, rely=0.3, anchor="center", height=50)
            
            submit.place(relx=0.5, rely=0.4, anchor="center",
                         height=40, width=70)
            enter.mainloop()
            
        def enter_field_data(subfield):
            def submit1():
                cursor.execute("insert into %s values('%s','%s',%s,'%s')"%(field_for_fun,company.get(),subfield.get(),experience.get(),contact.get()))
                mycon.commit()
                enter.destroy()
                admin1.destroy()
                table_window(field_for_fun)
                  
            enter = Tk()
            enter.geometry("920x720")
            
            #entry fields
            company = Entry(enter, width=50, borderwidth=3)
            subfield = Entry(enter, width=50, borderwidth=3)
            experience = Entry(enter, width=50, borderwidth=3)
            contact = Entry(enter, width=50, borderwidth=3)
            
            #button to execute the entry
            submit = Button(enter, text="Submit", command=submit1, borderwidth=3)
            
            company.insert(0, "enter company name")
            subfield.insert(0, "enter Job")
            experience.insert(0, "enter experience in years")
            contact.insert(0,"enter conatct")
            
            #to place the input fiels and other things
            company.place(relx=0.5, rely=0.2, anchor="center", height=50)
            subfield.place(relx=0.5, rely=0.3, anchor="center", height=50)
            experience.place(relx=0.5, rely=0.4, anchor="center", height=50)
            contact.place(relx=0.5, rely=0.5, anchor="center", height=40)
            submit.place(relx=0.5, rely=0.6, anchor="center", height=40,width=70)
            enter.mainloop()
             
        admin.destroy()
        
        def table_window(subfield):
            global admin1
            admin1 = Tk()
            admin1.geometry("920x720")
            global field_for_fun 
            field_for_fun = subfield
            cursor.execute("select * from %s"%(subfield))
            
            data = cursor.fetchall()
            #titles of table
            y0 = Label(admin1, width=20, height=3, text="Comapny", font='Helvetica 10 bold',
                      borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=0)
            
            y = Label(admin1, width=20, height=3, text="Job", font='Helvetica 10 bold',
                      borderwidth=2, relief='ridge', anchor="w").grid(row=0,column=1)
            
            y1 = Label(admin1, width=20, height=3, text="Experience in years", font='Helvetica 10 bold',
                      borderwidth=2, relief='ridge', anchor="w").grid(row=0,column=2)
            
            y2 = Label(admin1, width=20, height=3, text="Contact", font='Helvetica 10 bold',
                       borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=3)
            
            #loop to get the data from subfield table 
            i = 1
            for fields in data:
                for j in range(len(fields)):
                    e = Label(admin1, width=20, height=3, text=fields[j],
                              borderwidth=2, relief='ridge', anchor="w", font='Helvetica 10')
                    e.grid(row=i, column=j)
                i += 1
            
            def back1():
                admin1.destroy()
                admin_data()
                
            #button to execute command assigned
            back = Button(admin1, text="Back", borderwidth=3,
                          command=back1)
            remove = Button(admin1, text="remove", borderwidth=3,
                            command=lambda: remove_field_data(subfield))
            create = Button(admin1, text="create", borderwidth=3,
                            command=lambda: enter_field_data(subfield))
            remove.place(relx=0.87, rely=0.45, anchor="e", height=50, width=75)
            create.place(relx=0.87, rely=0.55, anchor="e", height=50, width=75)
            back.place(relx=0.87, rely=0.05, anchor="e", height=50, width=75)
            admin1.mainloop()
        if field == "IT":
            table_window("admin_itsubfield")
        elif field == "Design":
            table_window("admin_designsubfield")
        elif field == "Management":
            table_window("admin_managementsubfield")
                                   
    #to add heading
    title_field = Label(admin, text="Select Field")
    
    def logout1():
        admin.destroy()
        login()

    
    #to add buttons
    IT_button = Button(admin, text="IT", borderwidth=3,
                       command=lambda :field_type("IT"))
    Design_button = Button(admin, text="Design",
                           borderwidth=3, command=lambda :field_type("Design"))
    Managment_button = Button(admin, text="Management",
                              borderwidth=3, command=lambda: field_type("Management"))
    logout = Button(admin, text="Logout", borderwidth=3, command=logout1)
    
    #to position the buttons and title
    title_field.place(relx=0.4, rely=0.47,
                      anchor="center", height=50, width=75)
    IT_button.place(relx=0.4, rely=0.53, anchor="center", height=50, width=75)
    Design_button.place(relx=0.5, rely=0.53,
                        anchor="center", height=50, width=75)
    Managment_button.place(
        relx=0.6, rely=0.53, anchor="center", height=50, width=75)
    logout.place(
        relx=0.95, rely=0.05, anchor="ne", height=50, width=75)
    
    admin.mainloop()
#to see and display user data   
def user_data():
    user = Tk()
    user.geometry("920x720")
    
    def data():
        
        cursor.execute("select * from user_info where username = '%s'" %
                       (username))
        data = cursor.fetchall()
        global name_data, phone_no_data, experience_data , field_data
        name_data = data[0][0]
        phone_no_data = data[0][1]
        experience_data = data[0][2]
        field_data = data[0][3]
    data()
    
    #all the headings
    field = Label(user, width=20, height=3, text=f"Field: {field_data}",
                  borderwidth=2, anchor="center", font='Helvetica 15 bold').place(relx=0.77, rely=0.35)
    name = Label(user, width=20, height=3, text=f"Name: {name_data}",
                 borderwidth=2, anchor="center", font='Helvetica 15 bold').place(relx=0.77, rely=0.45)
    phone_no = Label(user, width=20, height=3, text=f"Phone_no: {phone_no_data}",
                     borderwidth=2, anchor="center", font='Helvetica 15 bold').place(relx=0.77, rely=0.55)
    experience = Label(user, width=20, height=3, text=f"Experience: {experience_data}",
                       borderwidth=2, anchor="center", font='Helvetica 15 bold').place(relx=0.77, rely=0.65)
    y0 = Label(user, width=20, height=3, text="Comapny", font='Helvetica 10 bold',
               borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=0)

    y = Label(user, width=20, height=3, text="Job", font='Helvetica 10 bold',
              borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=1)

    y1 = Label(user, width=20, height=3, text="Experience in years", font='Helvetica 10 bold',
               borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=2)

    y2 = Label(user, width=20, height=3, text="Contact", font='Helvetica 10 bold',
               borderwidth=2, relief='ridge', anchor="w").grid(row=0, column=3)
    
    #logout function
    def logout1():
        user.destroy()
        login()
    logout = Button(user, text="logout", command=logout1).place(
        relx=0.95, rely=0.05, anchor="ne", height=50, width=75)
    if field_type == "IT":
        work = "admin_itsubfield"
    elif field_type == "management":
        work = "admin_managementsubfield"
    else:
        work = "admin_designsubfield"
    
    cursor.execute("select * from %s" % (work))
    data = cursor.fetchall()
    
    #loop to execute the command
    i = 1
    for fields in data:
        for j in range(len(fields)):
            e = Label(user, width=20, height=3, text=fields[j],
                              borderwidth=2, relief='ridge', anchor="w", font='Helvetica 10')
            e.grid(row=i, column=j)
        i += 1
    

    user.mainloop()
#to enter login details    
def login():
    #to create a new window
    root = Tk()
    root.geometry('920x720')
    
    name_var = StringVar()
    passw_var = StringVar()
    
    def login_entry():
        global username,password
        username = name_var.get()
        password = passw_var.get()
        
        cursor.execute("select * from login_details where username = '%s' and password = '%s'"%(username,password))
        data = cursor.fetchall()
        #if new user is there
        global flag
        flag = False
        if not data:
            cursor.execute("insert into login_details VALUES('%s','%s')"%(username,password))
            mycon.commit()
            root.destroy()
            flag = True
            user_entry()
        #if admin is there
        elif data[0][0] == "shreyas_admin" and data[0][1] == "advanced_academy" :
            root.destroy()
            admin_data()
        #if old user is there
        else:
            
            root.destroy()
            user_data()   
            
    #to create input columns
    username_entry = Entry(root, textvariable=name_var,
                           width=50, borderwidth=3)
    password_entry = Entry(root,textvariable=passw_var,width=50,borderwidth=3)
    
    #to insert into blank input columns
    username_entry.insert(0,"Type your username")
    password_entry.insert(0, "Type your password")
    
    #to add a button
    submit_button = Button(root, text="Submit", borderwidth=3 , command=login_entry)
    
    #to position the things
    username_entry.place(relx=0.5, rely=0.46, anchor="center",height=50)
    password_entry.place(relx=0.5, rely=0.54, anchor="center",height=50)
    submit_button.place(relx=0.5, rely=0.62, anchor="center", width=75, height=50)
    
    #to get useraname and password all around the code)

        
    root.mainloop()
login()
