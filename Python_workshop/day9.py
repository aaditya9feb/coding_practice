# def demonstrate_string_functions():
#     s = "Hello, World!"

#     # Length of the string
#     print(f"Length of the string: {len(s)}")

#     # Convert to uppercase
#     print(f"Uppercase: {s.upper()}")

#     # Convert to lowercase
#     print(f"Lowercase: {s.lower()}")

#     # Check if string starts with a substring
#     print(f"Starts with 'Hello': {s.startswith('Hello')}")

#     # Check if string ends with a substring
#     print(f"Ends with 'World!': {s.endswith('World!')}")

#     # Find a substring
#     print(f"Find 'World': {s.find('World')}")

#     # Replace a substring
#     print(f"Replace 'World' with 'Universe': {s.replace('World', 'Universe')}")

#     # Split the string
#     print(f"Split by ', ': {s.split(', ')}")

#     # Join a list of strings
#     words = ['Hello', 'World']
#     print(f"Join list with space: {' '.join(words)}")

#     # Strip whitespace
#     s_with_spaces = "   Hello, World!   "
#     print(f"Strip whitespace: '{s_with_spaces.strip()}'")

# demonstrate_string_functions()

# l1=['san','man','tan']
# print(list(map(lambda x:x.capitalize(),l1)))

# # Convert to title case
# s2 = "hello, world!"
# print(f"Title case: {s2.title()}")
# # Convert list of strings to title case using map function
# l2 = ["hello, world!", "python programming", "openai gpt-3"]
# title_case_list = list(map(lambda x: x.title(), l2))
# print(f"Title case list: {title_case_list}")
# ###############################################################################################################################
# def menu():
#     print("Menu:")
#     print("1. Convert string to uppercase")
#     print("2. Convert string to lowercase")
#     print("3. Find a substring")
#     print("4. Count occurrences of a substring")
#     print("5. Replace a substring")
#     print("6. Split the string")
#     print("7. Strip whitespace")
#     print("8. Check if string starts with a substring")
#     print("9. Check if string ends with a substring")
#     print("10. Join a list of strings")
#     print("11. Check if string is alphabetic")
#     print("12. Check if string is numeric")
#     print("13. Check if string is alphanumeric")
#     print("14. Exit")

# def convert_string():
#     while True:
#         menu()
#         choice = input("Enter your choice (1-14): ")
#         if choice == '1':
#             s = input("Enter the string to convert to uppercase: ")
#             print(f"Uppercase: {s.upper()}")
#         elif choice == '2':
#             s = input("Enter the string to convert to lowercase: ")
#             print(f"Lowercase: {s.lower()}")
#         elif choice == '3':
#             s = input("Enter the string: ")
#             substring = input("Enter the substring to find: ")
#             index = s.find(substring)
#             if index != -1:
#                 print(f"Substring '{substring}' found at index {index}")
#             else:
#                 print(f"Substring '{substring}' not found")
#         elif choice == '4':
#             s = input("Enter the string: ")
#             substring = input("Enter the substring to count: ")
#             count = s.count(substring)
#             print(f"Substring '{substring}' occurs {count} times")
#         elif choice == '5':
#             s = input("Enter the string: ")
#             old_substring = input("Enter the substring to replace: ")
#             new_substring = input("Enter the new substring: ")
#             print(f"Replaced string: {s.replace(old_substring, new_substring)}")
#         elif choice == '6':
#             s = input("Enter the string to split: ")
#             delimiter = input("Enter the delimiter: ")
#             print(f"Split string: {s.split(delimiter)}")
#         elif choice == '7':
#             s = input("Enter the string with whitespace: ")
#             print(f"Stripped string: '{s.strip()}'")
#         elif choice == '8':
#             s = input("Enter the string: ")
#             substring = input("Enter the substring to check if it starts with: ")
#             print(f"Starts with '{substring}': {s.startswith(substring)}")
#         elif choice == '9':
#             s = input("Enter the string: ")
#             substring = input("Enter the substring to check if it ends with: ")
#             print(f"Ends with '{substring}': {s.endswith(substring)}")
#         elif choice == '10':
#             words = input("Enter a list of words separated by commas: ").split(',')
#             delimiter = input("Enter the delimiter to join the words: ")
#             print(f"Joined string: {delimiter.join(words)}")
#         elif choice == '11':
#             s = input("Enter the string: ")
#             print(f"Is alphabetic: {s.isalpha()}")
#         elif choice == '12':
#             s = input("Enter the string: ")
#             print(f"Is numeric: {s.isdigit()}")
#         elif choice == '13':
#             s = input("Enter the string: ")
#             print(f"Is alphanumeric: {s.isalnum()}")
#         elif choice == '14':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid Choice Please Try again")
# convert_string()
# ###########################################################################################################################3
def list_operations():
    my_list = []
    while True:
        print("\nList Operations Menu:")
        print("1. Append an element")
        print("2. Extend the list with another list")
        print("3. Insert an element at a specific position")
        print("4. Display the list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            element = input("Enter the element to append: ")
            my_list.append(element)
            print(f"Updated list: {my_list}")
        elif choice == '2':
            elements = input("Enter the elements to extend the list (comma-separated): ").split(',')
            my_list.extend(elements)
            print(f"Updated list: {my_list}")
        elif choice == '3':
            element = input("Enter the element to insert: ")
            position = int(input("Enter the position to insert the element at: "))
            my_list.insert(position, element)
            print(f"Updated list: {my_list}")
        elif choice == '4':
            print(f"Current list: {my_list}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

list_operations()

#################################################################################################################################

