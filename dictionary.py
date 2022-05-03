import json

choice = input("enter your choice: 1.Sign Up 2.Sign in 3.About")
if choice == "1":
    
    with open("jsd.json","w") as obj:
        mycred = {
            "username":"null",
            "password":"null",
            "name":"null",
            "contact": "null",
            "address": "null"

        }
        
        mycred["name"] = input("enter your Name")
        mycred["username"] = input("hello please enter username:")
        mycred["password"] = input("hello please enter password:")
        mycred["contact"] = input("enter your contact")
        mycred["address"] = input("enter your address")
        json.dump(mycred,obj)
    print("Sign Up successful")

if choice == "2":
    with open("jsd.json","r") as myfile:
    
	    result = json.load(myfile)

	    usr = input("hello please enter username:")
	    pswd = input("hello please enter password:")
	    if usr == result["username"] and pswd == result["password"]:
		    print("login success")
	    else:
		    print("login failed")

if choice == "3":
    with open("jsd.json","r") as myfile:
        result = json.load(myfile)
        print(result["name"])
        print(result["username"])
        print(result["password"])
        print(result["contact"])
        print(result["address"])
