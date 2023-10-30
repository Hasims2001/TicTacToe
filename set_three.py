# print("1. Tuple Unpacking")
# val = input("Enter List:")
# val = eval(val)
# for item in val:
#     print(f"{item[0]} is {item[1]} years old.")
# print("\n")



# print("2. Dictionary Manipulation")
# dist = {}
# opr = input("choose one (add, update, delete):")
# if(opr == 'add' or opr == 'update'):
#     val = input("enter name: age (key: value):").split(":")
#     dist.update({val[0].strip(): int(val[1].strip())})
#     print(dist)
# elif(opr == "delete"):
#     val = input("enter key:")
#     dist.pop(val.strip())
#     print(dist)
# else:
#     print("please choose correct option.")

# print("\n")


# print("3. Two Sum Problem")
# lists = eval(input("Enter List:"))
# target = int(input("Enter Target:"))
# lists.sort()
# i = 0
# j = len(lists)-1
# while(i<j):
#     sum = lists[i]+lists[j]
#     if(sum == target):
#         print("output:", [i, j])
#         break
#     elif(sum > target):
#         j -= 1
#     elif(sum < target):
#         i += 1

# print("\n")


# print("4. Palindrome Check")
# word = input("Enter String:")
# ind = 0
# rev = -1
# flag = True
# while(ind < len(word)):
#     if(word[ind] != word[rev]):
#         flag = False
#         break
#     ind += 1
#     rev -= 1

# if(flag):
#     print(f"{word} is Palindrome")
# else:
#     print(f"{word} is not Palindrome")

# print("\n")


# print("5. Selection Sort")
# lists = eval(input("Enter List:"))
# for i in range(0, len(lists)):
#     min = lists[i]
#     for j in range(i+1, len(lists)):
#         if(min > lists[j]):
#             min = lists[j]
#     store = min
#     min = lists[i]
#     lists[i] = store

# print(lists)
# print("\n")


print("6. Implement Stack using Queue")

print("\n")


print("7. FizzBuzz")
temp = ""
for i in range(1, 101):
    if(i%3 == 0 and i%5 == 0):
        temp += "FizzBuzz,"
    elif(i%3 == 0):
        temp += "Fizz,"
    elif(i%5 == 0):
        temp += "Buzz,"
    else:
        temp += str(i) + ","

print(temp)
print("\n")


print("8. File I/O")
inputFile = open("./input.txt", "r")
total = len(inputFile.read())
outputFile = open("./output.txt", "w")
outputFile.write(f"Number of words: {total}")
print(f"Number of words: {total}")
print("\n")


print("9. Exception Handling")
num1 =int(input("Num1:"))
num2 =int(input("Num2:"))
try:
    print(num1/num2)
except:
    print("Cannot divide by zero.")
print("\n")
