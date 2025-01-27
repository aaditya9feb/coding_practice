def oddEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def check_eligibility(age):
    if age >= 18:
        return "Eligible to vote."
    else:
        return "Not eligible to vote."

def greaterNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def checkVowel(char):
    if char in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

def checkPositive(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative"
    
def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"

def main():
    print("Enter the number: ")
    num = int(input())
    oddEven(num)
    print("Enter the age: ")
    age = int(input())
    print(check_eligibility(age))
    print("Enter the first number: ")
    num1 = int(input())
    print("Enter the second number: ")
    num2 = int(input())
    print(greaterNumber(num1, num2))
    print("Enter the character: ")
    char = input()
    print(checkVowel(char))
    print("Enter the number: ")
    num = int(input())
    print(checkPositive(num))
    print("Enter the year: ")
    year = int(input())
    print(leapYear(year))   

if __name__ == "__main__":
    main()