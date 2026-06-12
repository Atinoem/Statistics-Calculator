print("User Input Calculator")
data=input("Enter numbers seperated by spaces:")
numbers=[float(x) for x in data.split()]
numbers.sort()
print(numbers)
mid=(len(numbers))//2
if len(numbers)%2 ==1:
    median=numbers[mid]
else:
    median=(numbers[(mid-1)]+numbers[mid])/2
print("Median:",median)

