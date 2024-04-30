# class myClass:
#     x=5
    
# B2= myClass()
# print(B2.x)

class dayTrans:
    def __init__(self, name, phoneNumber, transaction):
        self.name = name
        self.phoneNumber = phoneNumber
        self.transaction = transaction
        

name = input("input Your Name: ")
phoneNumber = input("Input Your Phone Number: ")
transaction = input("Transaction Carried Out: ")

# cust1 = 0
# for c in range (6):
#     cust1 += 1
#     print(cust1)

cust1 = dayTrans(name, phoneNumber, transaction)
# print(cust1.name)
# print(cust1.phoneNumber)
# print(cust1.transaction)

# del (cust1) - This will read name error - Customer 1 is not defined
print(cust1.name, "a customer with Phone Number- ", cust1.phoneNumber, 
      "did", cust1.transaction)


