A=(input("do you want to start the program :"))
while(A=="yes"):
    num1=(int(input("enter a number :")))
    num2=(int(input("enter a number :")))
    choice=(int(input("choice :")))
    if(choice==1):
            print("Addition : ",num1+num2);
    elif(choice==2):
            print("Subtraction : ",num1-num2);
    elif(choice==3):
            print("Multiplication : ",num1*num2);
    elif(choice==4):
            print("Division : ",num1/num2);
    else:
        print("invalid choice");
    A=(input("do you want to continue :"))
