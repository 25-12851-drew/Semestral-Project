#BMI CALCULATOR

def get_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("===== BMI CALCULATOR =====")

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (meters): "))

            if weight <= 0 or height <= 0:
                print("Please enter positive numbers.")
                continue

            bmi = get_bmi(weight, height)
            category = get_category(bmi)

            print("\n===== BMI RESULT =====")
            print(f"Your BMI: {bmi:.2f}")
            print(f"Category: {category}")

            again = input("\nCalculate again? (yes/no): ").lower()

            if again != "yes":
                print("Thank you for using BMI Calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter numbers only.")

main()
