amount = int(input("Enter the amount:"))
no_of_100 = amount // 100
no_of_50 = (amount%100)//50
no_of_10 = ((amount%100)%50)//10

print("Number of 100 notes:", no_of_100)
print("Number of 50 notes:", no_of_50)
print("Number of 10 notes:", no_of_10)