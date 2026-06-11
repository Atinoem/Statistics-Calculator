print("User Input Calculator")
data=input("Enter numbers seperated by spaces:")
numbers=[float(x) for x in data.split()]
mean=sum(numbers)/len(numbers)
print("Numbers:",numbers)
print("Mean:",mean)