import json
def Authentication():
    name=input('enter name:-')
    pw=input("enter password")
    if len(pw)<6:
        print('length must be 6 digits')
        b=Authentication()
    elif len(pw)>15:
        print('length must be less than 15')
        b=Authentication()
    elif pw[0].isdigit():
        print('do not start with a digit')
        b=Authentication()
    else:
        up=0
        lo=0
        sc=0
        di=0
        ot=0
        spe='@#$%&?!'
        otr='/." "'
        i=0
        while i<len(pw):
            if pw[i].isupper():
                up+=1
            elif pw[i].islower():
                lo+=1
            elif pw[i].isdigit():
                di+=1
            elif pw[i] in spe:
                sc+=1
            elif pw[i] in otr:
                print("invalid password\ndo not use '/' ,'.' & space")
                b=Authentication()
            i+=1
        if ot>0:
            print("")        
        elif up>=1 and lo>1 and sc>=1 and di>=1:
            pw2=input("re-enter your password")
            if pw2==pw:
                with open("userDetails.json","r+") as f:
                    v=json.load(f)
                if v["user"]==[]:
                    d={name:pw}
                    v["user"].append(d)
                    with open("userDetails.json","w+") as file:
                        json.dump(v,file,indent=4)
                    print("congrats",name,"You are signed up successfully")
                else:
                    for i in v["user"]:
                        if name in i:
                            print("already exists")
                            b=Authentication()
                    else:
                        d={name:pw}
                        v["user"].append(d)
                        with open("userDetails.json","w+") as file:
                            json.dump(v,file,indent=4)
                        print("congrats",name,"You are signed up successfully")
                        with open("userDescrip.json",'r+') as file:
                            p2=json.load(file)
                        description=input("enter description:")
                        DOB=input("enter your dob:")
                        hobbies=input("enter your hobbies:")
                        gender=input("enter your gender:")
                        dic={"username":name,"password":pw,"profile":{"description":description,"dob":DOB,"hobbies":hobbies,"gender":gender}}
                        p2["user"].append(dic)
                        with open("userDescrip.json","w+") as f:
                            json.dump(p2,f,indent=4)
                        print("Thank You")
            else:
                print("both passwords are not same")
                b=Authentication()
        else:
            print('invalid password,at least password should contain one special character and one number.')
            b=Authentication()
def login():
    username=input('enter username:')
    password=input("enter password:")
    with open("userDescrip.json","r") as f:
        p=json.load(f)
    c=0
    for i in p["user"]:
        if i["username"]==username and i["password"]==password:
            print(username,"you are logged in successfully")
            print(i)
            c+=1
            log=input("type 'l' to logout:-")
            a=loginSignup()
    if c==0:
        print("invalid username & password")

def loginSignup():
    print("a. Login\nb. SignUp")
    user=input('select "a" or "b":-')
    if user=="a":
        f=login()
    elif user=="b":
        f=Authentication()
    else:
        print("choose a or b")
        f=loginSignup()
loginSignup()

