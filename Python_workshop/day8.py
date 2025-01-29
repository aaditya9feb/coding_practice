import pack.app.bakwass as bakwass
####Program to find alternate prine numbers upto a limit####

# def ifPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def alternatePrime(limit):
#     count = 0
#     for i in range(2, limit):
#         if ifPrime(i):
#             if count % 2 == 0:
#                 print(i, end=" ")
#             count += 1
#     print()
    
# alternatePrime(100)


######################################################################################################################

# Convert a decimal number to to a binary number

# def convertBinary(n):
#     n = int(n)
#     convert = bin(n)
#     convert=convert.replace("0b","")
#     return convert

# num=int(input("Enter a number: "))
# print(convertBinary(num))  # Output: 1010    

########################################################################################################################3

# def square(num):
#     return num*num

# l1=[1,2,3,4,5,6,7,8,9,10]

# squaredList = list(map(square, l1))
# print(squaredList)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# #######################################################################################################################3333
# def add2(num):
#     return num+2
# l1=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x+2, l1))) 
# l1=['1','2','3']
# print(l1)
# print(list(map(lambda x:int(x),l1)))# Output: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

########################################33333333333333333333333333333333333333333333333333333333333333333333333############


# str = input("Enter numbers seperated by space")
# l1=str.split()
# print(list(map(lambda x:int(x),l1)))
    
# def isStr(item):
#     return item.isalpha()

# l1=["1","abc","a1","asdfghj","sdfg12345"]

# filtered_list = list(filter(isStr, l1))
# print(filtered_list)

########################################################################################################################3

