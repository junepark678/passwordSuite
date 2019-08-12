import pickle, cryptography, hashlib
from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#with open("key.key", "wb") as keyFile:
#    pickle.dump(key, keyFile)

keyfile = open("key.key", "rb")
key = keyfile.read()
keyfile.close()

try:
    mode = int(input("what are you doing. Adding password: 1 seeing password: 2 "))
except KeyboardInterrupt:
    print("invalid")
    print("aborting")
    exit(130)
except ValueError:
    print("invalid")
    print("aborting")
    exit(1)


if mode==1:
    newPassName = input("What is the name of the place that you will use your password? ")

    newPassWord = input("What is the password? (this is all safe! I promise) ")

    newPassWord = newPassWord.encode()

    #newPassName = newPassName.encode()

    f: Fernet = Fernet(key)
    newPassWordEncrypted = f.encrypt(newPassWord)

    newPass = dict(passName=newPassName, passWord=newPassWordEncrypted)

    with open("%s.pickle" % newPassName, "wb") as f:
        pickle.dump(newPass, f)


elif mode==2:
    passName = input("What is the place you use the password ")

    with open("%s.pickle" % passName, "rb") as f:
        f2 = Fernet(key)
        dic = pickle.load(f)
        passWord = dic["passWord"]
        wordPass = f2.decrypt(token=passWord)
        wordPass = str(wordPass, "utf-8")
        dic = dict(passName = passName, passWord = wordPass)
        print(dic)