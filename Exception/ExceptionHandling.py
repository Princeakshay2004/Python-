
try:
    num= int(input("Enter Number :"))
    result=100 / num
    print(result)
except ZeroDivisionError:
    print("You Cant devide By Zero")
finally:
    print("Exception Complate")



