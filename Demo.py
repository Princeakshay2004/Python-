a = 5
b=6
print(a*b)

print(a+b)
print('Akshay')
print("Hello Akshay ")
a='Cocsit'
print(a[1:6:2])





count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
# while loop in python

i=0
while(i<4):
    print("Hello AKhsy")
    i=i+1

# for loop in python

for i in range(0,10):
    print(i)

    list=[1,2,3,4,5]
    for i in list:
        print(i)

# function in python

def print1(name):
    print("Hello ",name)

print1("Akshay")

# passing multipal args in function
def even_num(*num):
    for i in num:
        if(i%2==0):
            print("It is even number",i)
        else:
            print("It is odd number",i)

even_num(5,2,4,5,6,7,8,3,5,2,5,3,6,3,8)