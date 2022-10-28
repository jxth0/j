import random
fname = input("enter file name: ")
file = open("C:\\Users\\sli\\Desktop\\"+fname+".txt","x")
abc = "qwertyuioasdfghjkzxcvbnm1234567890"
#ABC = ["q","w"]
ABC = list(abc)
op = input("How many letters: ")
for i in range(100):
    name = ""
    for i in range(int(op)):
        name += ABC[random.randint(0,len(ABC))-1]
    print(name)
    file.write(name+"\n")
file.close()
