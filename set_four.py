# print("1. Anagram Check")
# str1 = input("str1:")
# str2 = input("str2:")
# if(sorted(str1) == sorted(str2)):
#     print("Strings are Anagram.")
# else:
#     print("Strings are not Anagram.")
# print("\n")


# print("2. Bubble Sort")
# lists = eval(input("Enter List:"))
# for i in range(0, len(lists)):
#     for j in range(0, len(lists)-i-1):
#         if(lists[j] > lists[j+1]):
#             store = lists[j]
#             lists[j] = lists[j+1]
#             lists[j+1] = store

# print(lists)
# print("\n")

# print("3. Longest Common Prefix")
# lists = eval(input("Enter List:"))
# size = len(lists)
# if(size == 0):
#     print("")
# elif(size == 1):
#     print(lists[0])
# else:
#     lists.sort()
#     end = min(len(lists[0]), len(lists[size-1]))
#     i = 0
#     while(i < end and lists[0][i] == lists[size-1][i]):
#         i += 1
#     print(lists[0][0:i])
# print("\n")

# print("4. String Permutations")
# def permutation(lists, curr, used):
#     if(len(curr) == len(lists)):
#         print(curr.join(""))
#         return
    

        

# print("\n")

# print("5. Implement Queue using Stack")
# print("\n")

# print("6. Missing Number")
# nums = eval(input("Enter list:"))
# nums.sort()
# print(nums)
# ind = 0
# for i in nums:
#     if(i != ind):
#         print(ind)
#         break
# print("\n")

# print("7. Climbing Stairs")
# top = int(input("Top:"))
# def findWays(top, ways, sum):
#     if(sum == top):
#         return 1
    
#     if(sum > top):
#         return 0
#     return findWays(top, ways+1, sum+1) + findWays(top, ways+1, sum+2)
# ways = 0
# sum = 0
# print(findWays(top, ways,  sum))
# print("\n")

print("")
print("\n")
print("9. Power of Two")
def PowerOfTwo(n):
    if n <= 0:
        return False
    
    set_bits = 0
    while n > 0:
        if n & 1 == 1:
            set_bits += 1
        n >>= 1  
    
    return set_bits == 1
print(PowerOfTwo(int(input("enter num:"))))
print("\n")

print("10. Contains Duplicate")
def contains_duplicate(nums):
    unique_set = set()

    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)

    return False

print(contains_duplicate(eval(input("enter list:"))))
print("\n")

print("")
print("\n")

print("")
print("\n")