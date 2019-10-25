def square():
    while True :
        try :
            num = int(input("Enter Number : ")) 
        except:# when user enter any type diffrint integer 
            print("An error occursd! Please sure you enter number!") 
        else:
            break
    print("Thank you, your number squared is: ",num**2)

square()