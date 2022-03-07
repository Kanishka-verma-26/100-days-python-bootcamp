import random
a=[]
let = int(input("How many letters do you want in your password?\n"))
sym = int(input("How many symbols do you want in your password?\n "))
n=int(input("How many numbers do you want in your password? \n"))
for i in range(let):
    z=random.randint(97,122)
    a.append(chr(z))
for i in range(sym):
    z=random.randint(33,47)
    a.append(chr(z))
for i in range(n):
    z=random.randint(48,57)
    a.append(chr(z))
print("".join(a))
random.shuffle(a)

print("Your passowrd is:","".join(a))