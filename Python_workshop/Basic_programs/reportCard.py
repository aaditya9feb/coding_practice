def get_marks():
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def calculate_sum(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_percentage(marks):
    return (sum(marks) / (len(marks) * 100)) * 100

def main():
    marks = get_marks()
    total = calculate_sum(marks)
    average = calculate_average(marks)
    percentage = calculate_percentage(marks)

    print("\nReport Card:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    main()