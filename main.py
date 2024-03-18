from connection import DatabaseConnection

class TaxCalculator:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.tax_slabs = [
            (300000, 0),
            (600000, 0.05),
            (900000, 0.1),
            (1200000, 0.2),
            (1500000, 0.3),
            (9999999999, 0.35)  # Assuming a flat rate of 35% for income above 15 lakhs
        ]

    def calculate_tax(self, income):
        tax = 0
        remaining_income = income

        for slab in self.tax_slabs:
            slab_income, slab_rate = slab
            if remaining_income <= 0:
                break
            taxable_amount = min(remaining_income, slab_income)
            tax += taxable_amount * slab_rate
            remaining_income -= slab_income

        return tax

    def get_tax_slab(self, income):
        for slab in self.tax_slabs:
            slab_income, _ = slab
            if income <= slab_income:
                return slab
        return self.tax_slabs[-1]

    def run(self):
        print("Welcome to the Tax Calculator CLI!")

        while True:
            choice = input("\nEnter '1' to calculate tax or '2' to exit: ")

            if choice == '1':
                income = float(input("Enter your annual income: ₹"))
                slab_income, slab_rate = self.get_tax_slab(income)
                tax_amount = self.calculate_tax(income)
                print(f"You fall in the {slab_rate*100}% tax slab for income up to ₹{slab_income:,}")
                print(f"Your tax amount is: ₹{tax_amount:,.2f}")

                user_data = {"income": income, "tax_amount": tax_amount}
                self.db_connection.insert_user(user_data)

            elif choice == '2':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    tax_calculator = TaxCalculator()
    tax_calculator.run()
