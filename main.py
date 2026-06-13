print("Mode Calculator")
data=input("Enter numbers seperated by spaces:")
numbers=[float(x) for x in data.split()]
numbers.sort()
print(numbers)
mode=max(numbers, key=numbers.count)
if numbers.count(mode) ==1:
   print("No Mode")
else:
   print("Mode:",mode)



