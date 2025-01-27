###Python program to reverse list###

'''

def reverse_list(input_list):
    return input_list[::-1]

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print("Original list:", sample_list)
    print("Reversed list:", reversed_list)
    
'''
###Python program to find the sum of digits in a number###
'''

def digits_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def main():
    num=1234
    sum = digits_sum(num)
    print(f"Sum of digits in {num} is {sum}")

if __name__ == "__main__":
    main()
    
'''

### Python program to take ASCII values of a string and multiply them###

'''
def asciiValueMultiply(string):
    result = 1
    for char in string:
        result *= ord(char)    ##ord() function returns the ASCII value of the character##
    return result

def main():
    string = "hello"
    result = asciiValueMultiply(string)
    print(f"Result of multiplying ASCII values of {string} is {result}")

if __name__ == "__main__":
    main()
    

'''
##Sir given question 13##



def main():
    string = "I am Santosh"
    result = string[5::]
    print(f"Good morning {result}")
    
if __name__ == "__main__":
    main()