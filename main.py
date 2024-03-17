#2
def display():
    #3
    def quit():
        frame.destroy()
        frame1.destroy()


    global a
    a = age.get()
    if 18 > int(a) >= 0 or 99> int(a) >40:
        frame1 = Tk()
        frame1.geometry("300x100")
        destry = Label(frame1,text = "We are sorry, you cant use this program!!").grid(row = 0,column = 2)
        b = Button(frame1,text='Quit Application',command=quit).grid(row = 2,column = 2)

    #4
    elif int(a) >= 18 and int(a) <= 50:
        #7
        def regorlog():


            # 10
            def login():

                # 11
                def check_presence():

                    # 12
                    def state_find():

                        #13
                        def city():

                            #14
                            def sector():

                                #15
                                def feedback():

                                    def criteria():

                                        fedbac = str([fb.get()])
                                        with open('FB.txt','a') as K:
                                            K.write(fedbac+'\n')
                                            messagebox.showinfo("","Thank You")
                                            with open("sectlink.txt", 'r') as file:
                                                for line in file:
                                                    if sec in line:
                                                        x = messagebox.askquestion("Redirecting",
                                                                                   "Redirecting to " + line + " site")
                                                        if x == "yes":
                                                            l = (line.split("="))[1]
                                                            import webbrowser
                                                            webbrowser.open(l)
                                                            break


                                    frame11 = Tk()
                                    frame11.geometry('500x500')
                                    fbLabel = Label(frame11,text = "Feedback about us").grid(row =0,column = 0)
                                    fb = StringVar()
                                    fbEntry = Entry(frame11,textvariable = fb).grid(row=1,column=0)
                                    fedbac = fb.get()
                                    but = Button(frame11,text = "Ok",command = criteria).grid(row = 2,column = 0)





                                global sec
                                sec = sectorr.get()
                                with open('secdetails.txt', 'r') as p:
                                    for lline in p:
                                        if sec in lline:
                                            frame10 = Tk()
                                            frame10.geometry('2000x500')
                                            ll = lline.split(";")
                                            k = 0
                                            for i in ll:
                                                secdetLabel = Label(frame10, text=i).grid(row=k, column=0)
                                                k+=1
                                            buton = Button(frame10, text="Done Reading", command=feedback).grid(row=7,
                                                                                                              column=0)
                                            break
                                    else:
                                        messagebox.showwarning("Warning", "Not found. Try Again!!")



                            f = open('States', 'r')
                            s = f.readlines()
                            global st
                            st = Statee.get()
                            for line in s:
                                if st in line:
                                    with open("Sectors.txt", 'r') as g:
                                        for linee in g:
                                            if st in linee:
                                                frame8.destroy()
                                                frame9 = Tk()
                                                frame9.geometry('1000x100')
                                                statelabel = Label(frame9,text = linee).grid(row = 0,column = 0)
                                                sectorLabel = Label(frame9,text = "Enter the sector chosen:").grid(row=1,column=0)
                                                sectorr = StringVar()
                                                sectorEntry = Entry(frame9,textvariable = sectorr).grid(row = 1,column =1)
                                                button = Button(frame9,text = "Ok",command = sector).grid(row = 2,column = 1)
                                                break
                                        else:
                                            messagebox.showwarning("Warning","State Not found. Try Again")





                        frame7.destroy()
                        frame8 = Tk()
                        frame8.geometry('400x100')
                        StateLabel = Label(frame8,text = "Enter your state:").grid(row = 0,column = 0)
                        Statee = StringVar()
                        StateEntry = Entry(frame8,textvariable = Statee).grid(row = 0,column = 1)
                        ok = Button(frame8,text = "Ok",command = city).grid(row = 1,column = 1)


                    #check presence
                    eid = emaill.get()
                    LD = open("logindetaile.txt", "r")
                    id = LD.read()
                    if eid in id:
                        frame6.destroy()
                        frame7 = Tk()
                        frame7.geometry('200x90')
                        Login_success = Label(frame7,text = "Successfully logged in").grid(row = 0,column = 0)
                        okk = Button(frame7,text = "Ok",command = state_find).grid(row = 1,column = 1)
                    else:
                        messagebox.showwarning("Warning", "Not found. Please Try Again!!")

                frame3.destroy()

                frame6 = Tk()
                frame6.geometry('500x200')

                # welcome back msg display
                backLabel = Label(frame6, text="WELCOME BACK!").grid(row=0, column=0)

                # typing in login details
                emailLabel = Label(frame6, text="Enter your email id to retrieve your details and past records:").grid(
                    row=1, column=0)
                emaill = StringVar()
                emailEntry = Entry(frame6, textvariable=emaill).grid(row=1, column=1)
                ko = Button(frame6, text="Ok", command=check_presence).grid(row=2, column=1)



            #8
            def register():
                frame3.destroy()

                #9
                def details_of_user():


                    #13_1
                    def state_find():

                        #14_1
                        def city():


                            #15_1
                            def sector():

                                #16_1
                                def feedback():

                                    def criteria():

                                        fedbac = str([fb.get()])
                                        with open('FB.txt', 'a') as K:
                                            K.write(fedbac + '\n')
                                            messagebox.showinfo("", "Thank You")
                                            with open("sectlink.txt", 'r') as file:
                                                for line in file:
                                                    if sec in line:
                                                        x = messagebox.askquestion("Redirecting",
                                                                                   "Redirecting to " + line + " site")
                                                        if x == "yes":
                                                            l = (line.split("="))[1]
                                                            import webbrowser
                                                            webbrowser.open(l)
                                                            break



                                    frame11 = Tk()
                                    frame11.geometry('500x500')
                                    fbLabel = Label(frame11, text="Feedback about us").grid(row=0, column=0)
                                    fb = StringVar()
                                    fbEntry = Entry(frame11, textvariable=fb).grid(row=1, column=0)
                                    fedbac = fb.get()
                                    but = Button(frame11, text="Ok", command=criteria).grid(row=2, column=0)



                                global sec
                                sec = sectorr.get()
                                with open('secdetails.txt', 'r') as p:
                                    for lline in p:
                                        if sec in lline:
                                            frame10 =Tk()
                                            frame10.geometry('2000x500')
                                            l = lline.split(";")
                                            k = 0
                                            for i in l:
                                                secdetLabel = Label(frame10, text=i).grid(row=k, column=0)
                                                k += 1
                                            but = Button(frame10, text="Done Reading", command=feedback).grid(row=7, column=0)
                                            break
                                    else:
                                        messagebox.showwarning("Warning","Not found. Try Again!!")





                            f = open('States', 'r')
                            s = f.readlines()
                            global st
                            st = Statee.get()
                            for line in s:
                                if st in line:
                                    with open("Sectors.txt", 'r') as g:
                                        for linee in g:
                                            if st in linee:
                                                frame8.destroy()
                                                frame9 = Tk()
                                                frame9.geometry('1000x100')
                                                statelabel = Label(frame9,text = linee).grid(row = 0,column = 0)
                                                sectorLabel = Label(frame9, text="Enter the sector chosen:").grid(row=1, column=0)
                                                sectorr = StringVar()
                                                sectorEntry = Entry(frame9, textvariable=sectorr).grid(row=1, column=1)
                                                button = Button(frame9,text = "Ok",command = sector).grid(row = 2,column = 0)
                                                break

                                        else:
                                            messagebox.showwarning("Warning","State Not found. Try Again")





                        frame8_1.destroy()
                        frame8 = Tk()
                        frame8.geometry('400x100')
                        StateLabel = Label(frame8,text = "Enter your state:").grid(row = 0,column = 0)
                        Statee = StringVar()
                        StateEntry = Entry(frame8,textvariable = Statee).grid(row = 0,column = 1)
                        ok = Button(frame8,text = "Ok",command = city).grid(row = 1,column = 1)




                    def detail(a, info2):  # file to save age,info1
                        logindetail = str([a, info2])
                        LD = open("logindetaile.txt", "a+")
                        LD.write(logindetail + "\n")
                        LD.close()


                    frame5.destroy()
                    # displaying user details
                    global name
                    global eid
                    name = namee.get()
                    eid = eeid.get()
                    frame8_1 = Tk()
                    frame8_1.geometry('500x500')
                    check_detailLabel = Label(frame8_1,text="Check your details"+"\n"+"Your name: " + name + '\n' + "Your age: " + a + '\n' + "Your email: " + eid + '\n' + "Your random-id: " + str(ID)).grid(row=0 ,column = 0)
                    info2 = [name, eid, ID]
                    detail(a, info2)
                    button = Button(frame8_1,text = "Ok",command = state_find).grid(row = 1,column = 1)




                frame5 = Tk()
                frame5.geometry('500x400')

                #name entry
                nameLabel = Label(frame5,text = "Your name:").grid(row = 0,column = 0)
                namee = StringVar()
                nameEntry = Entry(frame5,textvariable = namee).grid(row = 0,column = 1)



                #email entry
                eidLabel = Label(frame5,text = "Your email-id:").grid(row = 1,column = 0)
                eeid = StringVar()
                eidEntry = Entry(frame5,textvariable = eeid).grid(row = 1,column = 1)



                #random id generation
                import random
                idf = random.random()
                ids = random.randint(0, 100)
                global ID
                ID = idf + ids * 1000
                idLabel = Label(frame5,text = "Your random-id: "+str(ID)).grid(row = 2,column = 0)
                b = Button(frame5,text = "Done",command = details_of_user).grid(row = 3,column = 1)





            frame3 = Tk()
            frame3.geometry("500x200")
            r_or_l = Label(frame3,text = "Register or Login").grid(row = 0,column = 0)
            register = Button(frame3, text = "Register",command = register ).grid(row = 2,column = 1)
            login =  Button(frame3, text = "Login",command = login).grid(row = 2,column = 2)






        #6
        def quit1():


            def quit2():
                frame4.destroy()

            #inner quit
            frame2.destroy()
            frame4 = Tk()
            frame4.geometry("500x200")
            exit = Label(frame4,text = "Not registering yourself would mean you will not be able to use this program.\n"
                                       "Are you sure you do not want to register?").grid(row = 0,column = 0)
            yes = Button(frame4, text="Yes", command=quit2).grid(row=1, column=1)
            no = Button(frame4, text='No', command=regorlog).grid(row=1, column=2)

        #5
        #inner main
        messagebox.showinfo("About us","We are trying to provide jobs for youngsters who are awaiting to get their salaries.\nWe have provided jobs for large number of people who further poped out with success.\nWe have been awarded as the number one job assistant in our country.\nWe have incorporated several options for the user to get a good job for which they have been awaiting for.\nWhile selecting the job it is important that one is well aware of the perks that come along with the job.\nWe are aimed to provide user with the idea about the jobs available in a selected city.\nWith just few clicks the user will get all basic information about the job they are looking forward!\nWe hope that this would help you to get a job for which you have been looking for!!")

        frame2 = Tk()
        frame2.geometry("500x200")

        # register or login
        frame.destroy()
        r= Label(frame2, text="This takes you to register or login window.\nDo you want to go ahead?").grid(row=0, column=0)
        yes = Button(frame2, text='Yes', command= regorlog).grid(row=1, column=1)
        no = Button(frame2, text = "No",command = quit1).grid(row = 1, column = 2)
        '''        
        b = Button(frame2,
                   text='Quit Application',
                   command=call)

        canvas.create_window(100, 100,
                             window=b)'''

    else :
        messagebox.showwarning("Warning",'Check Your input and Try Again')


#1
from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.geometry("500x200")

#age
ageLabel = Label(frame, text="Please enter your age").grid(row=0, column=0)
age = StringVar()
ageEntry = Entry(frame, textvariable=age).grid(row=0, column=1)


#done button
agebutton = Button(frame,text = 'Done', command = display).grid(row=1, column = 1)
frame.mainloop()
