# simpleInterest.py

def calculate_simple_interest(principal, rate, time):
   
    interest = (principal * rate * time) / 100
    return interest

# Example usage
if __name__ == "__main__":
    principal_amount = float(input("Enter the principal amount: "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    time_period = float(input("Enter the time period in years: "))

    interest = calculate_simple_interest(principal_amount, annual_rate, time_period)
    print(f"The simple interest is: {interest}")