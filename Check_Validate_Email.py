print("Email Validate Checker")
print("Create By Zubair")
k=0
j=0
d=0
email = input("Enter the Email: ") 
if len(email)>=6:
    if email[0].isalpha():
        if "@" in email and email.count('@')==1:
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "@" or i == ".":
                        continue
                    else:
                        d=1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Email! 3")
                else:
                    print("Valid Email")
            else:
                print("Ivalid Email! 2")
        else:
            print("Invalid Email! 1")
    else:
        print("Invalid Email! First letter Must be Alpabet")
else:
    print("Wrong Email because less then 6 character")