import secrets
import string
import random
alphabet=''
digits=''
sp_char=''
p=[]
l=int(input("enter length of password: "))
for i in range(l):
    ch=int(input("enter choice 1:alphabets 2:digits 3:special charecter: 1"))
    if ch==1:
        alphabet=secrets.choice(string.ascii_letters)
        p.append(alphabet)
    elif ch==2:
        digits=secrets.choice(string.digits)
        p.append(digits)
    elif ch==3:
        sp_char=secrets.choice(string.punctuation)
        p.append(sp_char)
    else:
        print("invalid input")


temp=''
password=''
temp=temp.join(p)

password=password.join(random.sample(temp,len(temp)))

print(password)
