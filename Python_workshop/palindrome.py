##Python program to check if number is palindrome or not##

def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]


def main():
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

if __name__ == "__main__":
    main()