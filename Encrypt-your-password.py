
def passwordgenerator(password,key):
    EncryptPassword = ""
    newpassword = []
    for x in password:
        q = ord(x)
        if q+key >126:
            first = 126-q
            second = key - first
            newpassword.append(chr(33+second-1))
        else:
            newpassword.append(chr(q+key))
    EncryptPassword = "".join(newpassword)     
    return EncryptPassword
if __name__ == "__main__":
    keysum = 0
    password = input("Enter Your password")
    key = list(map(int,input("Enter Your Four digit Key  ")))
    for x in key:
        keysum+=x
    n = passwordgenerator(password,keysum)
    print(n,type(n))
    
    
    