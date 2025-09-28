class CustomError(Exception):
    pass

def Stock_Quentity(Quantity):
    stock=100
    if Quantity >  stock:
        raise CustomError(' Quatity is Too Much As Greather Than Stock')
    else:
        print("Stock is  available")

try:
    num=int(input("Enter Quantity :"))
    Stock_Quentity(num)
except CustomError as e:
    print(e)




