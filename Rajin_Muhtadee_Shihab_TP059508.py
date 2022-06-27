# INDIVIDUAL ASSIGNMENT
# CT108-3-1-PYP
# APD1F2009CS
# Name : RAJIN MUHTADEE SHIHAB
# TP : TP059508


### Main Menu Code

def mainmenu():

    print("\t\tWELCOME TO REAL CHAMPIONS SPORT ACADEMY")
    print("\n\nChoose User Type (1/2)\n\n1. ADMIN\n2. STUDENT\n0. Terminate Program")

    menuc1 = int(input("\nEnter Your Choice : "))
    
    if (menuc1 == 1):
        print("\n\t\tYou've Chosen The Admin User Type")
        adminmenu1()
        
    elif (menuc1 == 2):
        print("\n\t\tYou've Chosen The Student User Type")
        studentmenu1()
        
    elif (menuc1 == 0):
        print("Program Terminated. Good Bye!")
        
    else :
        print("\n\t\tWrong Input")
        mainmenu()

### Admin Menu Login Code [Password : 92125]


def adminmenu1():
    
    print("\n\n\t\tLOGIN TO USE ADMIN SYSTEMS")
    
    adminpass = int(input("\n\nPlease Enter The Admin System Password : "))

    if (adminpass == 92125):
        print("\n\t\tLogin Successful")
        adminmenu2()
    else :
        print("Wrong Password!")
        adminmenu1()

### Admin Menu Code


def adminmenu2():

    print("\n\n\t\tWELCOME TO REAL CHAMPIONS SPORT ACADEMY ADMIN SYSTEMS")
    print("\n\n\t\tHere Are The Functionalities!")
    print("\n\n1. Add Records of \n\n\t11. Coach\n\t12. Sport\n\t13. Sport Schedule\n\n2. Display All Records of\n\n\t21. Coach\n\t22. Sport\n\t23. Registered Students\n\t24. Coach Feedback"
          "\n\n3. Search Specific Records of\n\n\t31. Coach by Coach ID\n\t32. Coach by Overall Performance (Rating)\n\t33. Sport by Sport ID\n\t34. Student by Student ID"
          "\n\n4. Sort and display Record of\n\n\t41. Coaches in Ascending Order by Names.\n\t42. Coaches Hourly Pay Rate in Ascending Order\n\t43. Coaches Overall Performance in ascending order"
          "\n\n5. Modify Record of\n\n\t51. Coach\n\t52. Sport\n\t53. Sport Schedule\n\n00. Exit")

    adminc1 = int(input("\nEnter Your Choice [FE : 12 / 22 / 43] : "))

    if (adminc1 == 11):
        addcoach()
    elif (adminc1 == 12):
        addsport()
    elif (adminc1 == 13):
        addschedule()
    elif (adminc1 == 21):
        discoach()
    elif (adminc1 == 22):
        dissports()
    elif (adminc1 == 23):
        disregstud()
    elif (adminc1 == 24):
        discoachfeed()
    elif (adminc1 == 31):
        discoachid()
    elif (adminc1 == 32):
        discoachperf()
    elif (adminc1 == 33):
        dissportid()
    elif (adminc1 == 34):
        disstudid()
    elif (adminc1 == 41):
        sortname()
    elif (adminc1 == 42):
        sortpay()
    elif (adminc1 == 43):
        sortperf()
    elif (adminc1 == 51):
        modcoach()
    elif (adminc1 == 52):
        modsport()
    elif (adminc1 == 53):
        modschedule()
    elif (adminc1 == 00):
        mainmenu()        
    
### Coach Addition Code [ADMIN 11]
        
def addcoach():

    print("\n\n\t\tCoach Records")
    '''
    coachrec = open("CoachRecords.txt","wt")#-------------------------------------------------------------- File Creation Code
    '''
    coachrec = open("CoachRecords.txt","a")
    print("\n\n\t\tEnter Coach Details")
    Coachid = str(input("Coach ID : "))
    Name = str(input("Name : "))
    DOB = str(input("Date of Birth : "))
    Sport = str(input("Sport : "))
    Spcode = str(input("Sport Code : "))
    Location = str(input("Location : "))
    Hrate = str(input("Hourly Rate : "))
    Jdate = str(input("Joining Date : "))
    rate = str(input("Enter Initial Rating [ 1 / 2 / 3 / 4 / 5 ] : "))
    phone = str(input("Phone Number : "))
    coachrec.write("\n"+Coachid+"\t"+Name+"\t"+DOB+"\t"+Sport+"\t"+Spcode+"\t"+Location+"\t"+Hrate+"\t"+Jdate+"\t"+phone)          
    coachrec.close()                 

    X = int(input("Do You Want To Continue? [0 / 1] : "))
    if (X == 0):
        adminmenu2()
    elif (X == 1):
        addcoach()
    else :
        print("Wrong Input")
        mainmenu()
        
### Sport Addition Code [ADMIN 12]

def addsport():

    print("\n\n\t\tSport Records")
    '''
    #sportrec = open("Sport Records.txt","wt")#--------------------------------------------------------------- File Creation Code
    '''
    sportrec = open("Sport Records.txt","a")
    print("\n\n\t\tEnter Sport Details")
    Name = str(input("Enter Sport Name : "))
    Spcode = str(input("Enter Sport Code : "))
    Location = str(input("Enter Location : "))

    sportrec.write("\n"+Spcode+"\t"+Name+"\t"+Location)
    sportrec.close()

    X = int(input("Do You Want To Continue? [0 / 1] : "))
    if (X == 0):
        adminmenu2()
    elif (X == 1):
        addsport()
    else :
        print("Wrong Input")
        mainmenu()
        
### Sport Schedule Addition Code [ADMIN 13]

def addschedule():

    print("\n\n\t\tSport Schedule")
    '''
    spsche = open("Sport Schedule.txt","wt")#--------------------------------------------------------------- File Creation Code
    spsche.write("Sport_Code\tSport\tLocation\tWeekdays\tTime [GMT +8]")
    '''             
    spsche = open("Sport Schedule.txt","a")
    print("\n\n\t\tEnter Sport Schedule Details")
    Spcode = str(input("Enter Sport Code : "))
    Name = str(input("Enter Sport Name : "))
    Location = str(input("Enter Location : "))
    Wkday = str(input("Enter Day of The Week [1 Max] : "))
    Time = str(input("Enter Time of The Day [HH:MM AM/PM] : "))
    

    spsche.write(Spcode+"\t"+Name+"\t"+Location+"\t"+Wkday+"\t"+Time)
    spsche.close()

    X = int(input("Do You Want To Continue? [0 / 1] : "))
    if (X == 0):
        adminmenu2()
    elif (X == 1):
        addschedule()
    else :
        print("Wrong Input")
        mainmenu()
                     
    
### Display Records Code

def discoach(): #Display Coach Records [ADMIN 21]

    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    coachrec = open("CoachRecords.txt","rt")
    
    #for line in coachrec:
        #data = line.split()    # Splits on whitespace
        #print(("{0[0]:<8}{0[1]:<10}{0[2]:<10}{0[3]:<15}{0[4]:<10}{0[5]:<10}{0[6]:<10}{0[7]:<15}{0[8]:<10}{0[9]:<15}").format(data))
    print(coachrec.read())
    coachrec.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
    
        
def dissports(): #Display Sport Records [ADMIN 22]

    sportrec = open("Sport Records.txt","rt")
    print("\n"+sportrec.read())
    sportrec.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")

def disregstud(): #Display Registered Student Records [Admin 23]

    studregrec = open("Student Records.txt","rt")
    print("\n"+studregrec.read())   
    studregrec.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")

def discoachfeed(): #Display Coach Feedback [ADMIN 24]
    
    fback = open("Feedback.txt","rt")
    print("\n"+fback.read())
    fback.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")        
    
### Search Specific Records Code

def discoachid(): #Coach By Coach ID [ADMIN 31]
    
    a = 0 # Dummy variable
    
    coachrec = open("CoachRecords.txt","rt")
    
    sid = str(input("\n\nEnter Coach ID To Search : "))
    
    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    for line in coachrec:
        if sid in line:
            print(line)
            a = a + 1
    if (a == 0):
         print("Entry Not Found. Try Again")
         discoachid()
                
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
        
    coachrec.close()            

def discoachperf(): #Coach By Performance [ADMIN 32]

    a = 0 # Dummy Variable
    
    coachrec = open("CoachRecords.txt","rt")
    
    rate = str(input("\n\nEnter Coach Rating To Search [1 / 2 / 3 / 4 / 5] : "))

    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")

    for line in coachrec:
        f = line
        line = line.split("\t")
        if rate in line[8]:
            print(f)
            a = a + 1

    if (a == 0):
         print("Entry Not Found. Try Again")
         discoachperf()
         
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
    
    coachrec.close() 

def dissportid(): #Sport By Sport ID [ADMIN 33]

    a = 0 # Dummy Variable
    
    sportrec = open("Sport Records.txt","rt")

    spid = input("\n\nEnter Sport Code To Search : ")

    print("\n"+sportrec.readline())
    
    for line in sportrec:
        if spid in line:
            print(line)
            a = a + 1

    if a == 0 : # Dummy Condition
        print("Entry Not Found")
        dissportid()
        
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
        
    sportrec.close()
        
           

def disstudid(): #Student By Student ID [ADMIN 34]

    a = 0

    studrec = open("Student Records.txt","rt")

    stid = input("\n\nEnter Student ID To Search [F.E : CSAXXXX] : ")

    print("\n"+studrec.readline())

    for line in studrec:
        if stid in line:
            print(line)
            a = a + 1

    if (a == 0):
        print("Entry Not Found. Try Again")
        disstudid()

    studrec.close()
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
            
###  Sort and display Record Code

#Coach Sort By Name [ ADMIN 41 ]

def sortname():
    sortlist=[]
    coachrec = open ("CoachRecords.txt","rt")
    for line in coachrec:
        line = line.split("\t")
        sortlist.append(line[1])
    a = True # Dummy 
    while a:
        a = False
        for cnt in range(len(sortlist)-1):
            if sortlist[cnt] > sortlist[cnt+1]:
                aux = sortlist[cnt]
                sortlist[cnt] = sortlist[cnt+1]
                sortlist[cnt+1] = aux
                a = True
    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    for x in sortlist:
        coachrec = open("CoachRecords.txt", "rt")
        for line in coachrec:
            temp = line
            line = line.split("\t")
            if x in line[1]:
                print("\n"+temp)

    coachrec.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")    

# Coach Sort By Hourly Pay Rate

def sortpay():
    sortlist=[]
    coachrec = open ("CoachRecords.txt","rt")
    for line in coachrec:
        line = line.split("\t")
        sortlist.append(line[6])
    a = True # Dummy 
    while a:
        a = False
        for cnt in range(0, len(sortlist)-1):
            
            if sortlist[cnt] > sortlist[cnt+1]:
                aux = sortlist[cnt]
                sortlist[cnt] = sortlist[cnt+1]
                sortlist[cnt+1] = aux
                a = True
                
    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    for x in sortlist:
        coachrec = open("CoachRecords.txt", "rt")
        for line in coachrec:
            temp = line
            line = line.split("\t")
            if x in line[6]:
                print("\n"+temp)
                
    coachrec.close()
    
    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")        

# Coach Sort By Rating

def sortperf():
    sortlist=[]
    coachrec = open ("CoachRecords.txt","rt")
    for line in coachrec:
        line = line.split("\t")
        sortlist.append(line[8])
    a = True # Dummy 
    while a:
        a = False
        for cnt in range(0, len(sortlist)-1):
            
            if sortlist[cnt] > sortlist[cnt+1]:
                aux = sortlist[cnt]
                sortlist[cnt] = sortlist[cnt+1]
                sortlist[cnt+1] = aux
                a = True
                
    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    for x in sortlist:
        coachrec = open("CoachRecords.txt", "rt")
        for line in coachrec:
            temp = line
            line = line.split("\t")
            if x in line[8]:
                print("\n"+temp)
           
    coachrec.close()

    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
        
### Modifying Records Code

# Modifying Coach Records [ADMIN 51]

def modcoach():

    print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
    coachrec = open("CoachRecords.txt", "rt")
    print("\n"+coachrec.read())
    coachrec.close()
    coachrec = open("CoachRecords.txt", "rt")
    O = str(input("Enter The Word : "))
    Y = str(input("Replacement : "))
    temp = open("out.txt", "wt")
    for line in coachrec:
        temp.write(line.replace(O, Y))
    coachrec.close()
    temp.close()
    temp = open("out.txt", "rt")
    coachrec = open("CoachRecords.txt", "wt")
    for line in temp:
        coachrec.write(line)
    temp.close()
    coachrec.close()

    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
   
#Modifying Sport Records [ADMIN 52]

def modsport() :
    
    print("\nSport Name\tSport Code\tLocation")
    sportrec = open("Sport Records.txt", "rt")
    print("\n"+sportrec.read())
    sportrec.close()
    sportrec = open("Sport Records.txt", "rt")
    O = str(input("Choose The Entry : "))
    Y = str(input("Replacement : "))
    temp = open("out.txt", "wt")
    for line in sportrec:
        temp.write(line.replace(O, Y))
    sportrec.close()
    temp.close()
    temp = open("out.txt", "rt")
    sportrec = open("Sport Records.txt", "wt")
    for line in temp:
        sportrec.write(line)
    temp.close()
    sportrec.close()

    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")
  
    
# Modifying Sport Schedule [ADMIN 53]

def modschedule():

    spsche = open("Sport Schedule.txt", "rt")
    print("\n"+spsche.read())
    spsche.close()
    spsche = open("Sport Schedule.txt", "rt")
    O = str(input("Choose The Entry : "))
    Y = str(input("Replacement : "))
    temp = open("out.txt", "wt")
    for line in spsche:
        temp.write(line.replace(O, Y))
    spsche.close()
    temp.close()
    temp = open("out.txt", "rt")
    spsche = open("Sport Schedule.txt", "wt")
    for line in temp:
        spsche.write(line)
    temp.close()
    spsche.close()

    X = int(input("Go Back To Admin? [0 / 1] : "))
    if (X == 1):
        adminmenu2()
    elif (X == 0):
        print("Good Bye!")

################################################################################################################################################################################################

### Student Menu Code

def studentmenu1():

    print("\n\n\t\tWELCOME TO REAL CHAMPIONS SPORT ACADEMY STUDENT SECTION")
    print("\nStudent Type\n\n1. Registered\n2. New / Non-Registered\n0. Exit")

    studentc1 = int(input("\nChoose Student Type [0 / 1 / 2] : "))

    if (studentc1 == 1):
        studentmenu2()
    elif (studentc1 == 2):
        studentmenu3()
    elif (studentc1 == 0):
        mainmenu()   
    else :        
        print("Wrong Input")
        studentmenu1()


### Student Records        

# Student Regirstration Code

def studreg():

    print("\n\n\t\tWelcome To Registration Terminal")
    '''
    studrec = open("Student Records.txt","wt") #--------------------------------------------------------------- File Creation Code
    studrec.write("Student_ID\tName\tDOB\tSport")
    '''
    studrec = open("Student Records.txt","a")    

    unid = str(input("Create A Student ID [F.E : CSAXXXX] : "))
    name = str(input("Enter Your Name : "))
    dob = str(input("Enter Your Date of Birth : "))
    sport = str(input("Enter Sport Name : "))
    phone = str(input("Enter Your Phone Number : "))
    
    studrec.write("\n"+unid+"\t"+name+"\t"+dob+"\t"+sport)
    studrec.close()
    
    X = int(input("Do You Want To Continue? [0 / 1] : "))
    if (X == 0):
        studentmenu1()
    elif (X == 1):
        studentmenu2()
    else :
        print("Wrong Input")
        mainmenu()


### Registered Student Menu Login Code [ Password - Student ID ]

def studentmenu2():
    
    print("\n\n\t\tLOGIN TO USE STUDENT SYSTEMS")

    a = 0 # Dummy variable
    
    studregrec = open("Student Records.txt","rt")
    
    stdpass = str(input("\n\nPlease Enter Your Student ID [F.E : CSAXXXX] : "))
    
    for line in studregrec:
        if stdpass in line:
            print("\n\n\t\tWelcome To The Student System Student "+stdpass)  
            print("\n\nFunctionalities\n\n1. View Coach Details\n2. View Sport Details\n3. View Registered Sport Schedule\n4. View Self Record\n5. Modify Self Record\n6. Coach Feedback")

            X = int(input("\n\nEnter Your Choice : "))

            if (X == 1):

                print("\nCoach_ID\tName\tDOB\tSport\tSport_Code\tLocation\tHourly_Rate\tJoined\tRating\tPhone")
                coachrec = open("CoachRecords.txt","rt")
                print(coachrec.read())
                coachrec.close()
                
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")

            elif (X == 2):

                print("\nSport Name\tSport Code\tLocation")
                sportrec = open("Sport Records.txt","rt")
                print(sportrec.read())
                sportrec.close()
                
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")
                    
            elif (X == 3):
                
                studregrec = open("Student Records.txt","rt")
                for line in studregrec:
                    line = line.strip()
                    x = line.split("\t")
                    if stdpass == x[0]:
                        Y = (x[3])

                spsche = open("Sport Schedule.txt","rt")
                print("\n"+spsche.readline())
                for line in spsche:
                    if Y in line:
                        print (line)
                        
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")
                
            elif (X == 4):
        
                studregrec = open("Student Records.txt","rt")
                print("\n"+studregrec.readline())
                studregrec.close()
                studregrec = open("Student Records.txt","rt")
                for line in studregrec:
                    line = line.strip()
                    x = line.split("\t")
                    if stdpass == x[0]:
                        print("\n",x[0],"\t",x[1],"\t",x[2],"\t",x[3])
                        
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")

            elif (X == 5):
                
                studregrec = open("Student Records.txt", "rt")
                print("\n"+studregrec.readline())
                studregrec.close()
                studregrec = open("Student Records.txt", "rt")
                for line in studregrec:
                    if stdpass in line:
                        print(line)
                studregrec.close()
                
                studregrec = open("Student Records.txt", "rt")    
                O = str(input("Choose The Entry : "))
                Y = str(input("Replacement : "))
                temp = open("out.txt", "wt")
                for line in studregrec:
                    temp.write(line.replace(O, Y))
                studregrec.close()
                temp.close()
                temp = open("out.txt", "rt")
                studregrec = open("Student Records.txt", "wt")
                for line in temp:
                    studregrec.write(line)
                temp.close()
                studregrec.close()
                
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")
                    
            elif (X == 6):
                '''
                fback = open("Feedback.txt","wt") #-------------------------------------------------------------------File Creation Code
                fback.write("Student ID\tCoach ID\t\tRating\tFeedback")
                '''
                fback = open("Feedback.txt","a")
                cid = str(input("Enter Coach ID : "))
                rate = str(input("Rating [ 1 - 5 ] : "))
                tfeed = str(input("How Was Your Experience With This Coach? : "))
                fback.write("\n"+stdpass+"\t\t"+cid+"\t\t"+rate+"\t"+tfeed)
                fback.close()
                
                F = int(input("\nContinue? [0 / 1] : "))
                if (F == 1):
                    studentmenu2()
                elif (F == 0):
                    print("Good Bye!")               
         

### Unregistered Student Menu

def studentmenu3():

    print("\n\n\t\tWelcome To The Student Section")
    print("\n\nThe Functionalities Are\n\n1. Register\n2. Sport Details\n3. Sport Schedule\n0. Exit")

    X = int(input("Enter Your Choice : "))

    if (X == 1):
        studreg()

    elif (X == 2):

        print("\nSport Name\tSport Code\tLocation")
        sportrec = open("Sport Records.txt","rt")
        print("\n"+sportrec.read())
        F = int(input("\nContinue? [0 / 1] : "))
        if (F == 1):
            studentmenu3()
        elif (F == 0):
            print("Good Bye!")                
        
    elif (X == 3):

        spsche = open("Sport Schedule.txt","rt")
        print("\n"+spsche.read())
        F = int(input("\nContinue? [0 / 1] : "))
        if (F == 1):
            studentmenu3()
        elif (F == 0):
            print("Good Bye!")
    
    elif (X == 0):
        studentmenu1()
        
    else :
        print("\nWrong input")
        studentmenu3()
        
    
    

    
mainmenu()         
              
          
    

    
       
