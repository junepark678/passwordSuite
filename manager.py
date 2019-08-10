import pickle

try:
    mode = int(input("what are you doing. Adding password: 1 seeing password: 2 "))
except:
    print("invalid")
    print("aborting")
    exit()


if mode==1:
    newPassName = input("What is the name of the place that you will use your password? ")

    newPassWord = input("What is the password? (this is all safe! I promise) ")

    newPass = dict(passName=newPassName, passWord=newPassWord)

    with open("%s.pickle" % newPassName, "wb") as f:
        pickle.dump(newPass, f)

elif mode==2:
    passName = input("What is the place you use the passname ")
    with open("%s.pickle" % passName, "rb") as f:
        print(pickle.load(f))