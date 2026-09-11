student={}

while True:
    print("-----STUDENT MANAGER APP----- ")
    print("1.add student")
    print("2.view student")
    print("3.check result")
    print("5.exit")

    choice=input("ENTER YOUR CHOICE: ")
    #Add student
    if choice=="1":
        name=input("enter the name of the student:")
        mark=int(input("enter the mark of the student:"))
        student[name]=mark
        print(f"{student} is succesfully added")
    #view student
    elif choice=="2":
        if not student:
            print("no student is found")
        else:
            for name,marks in student.items():
                print(name,":",marks)

    elif choice=="3":
        name = input("enter the name of the student: ")
        if name in student:
            mark = student[name]
            if mark >= 35:
                print("student pass the exam")
            else:
                print("student fail the exam")
        else:
            print("student not found")

    elif choice=="4":
        print("exiting")
        break
    else:
        print("invalid input")


          
             







