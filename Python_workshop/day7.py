### Program TO find the sum of elements in a list ###
# def sumList(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum


# list = [1,2,3,4,5,6,7,8,9,10]
# print(sumList(list))
    

######################################################################################################

def findEvenNumbers(list):
    even_numbers = []
    for i in list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

list=[1,2,3,4,5,6,7,8,9,10]
print(findEvenNumbers(list))

######################################################################################################

def name(name):
    def stars():
        print("************")
    stars()
    print(name)
    stars()
    
name("Aaditya")
