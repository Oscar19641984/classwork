class SavingsPlan:
    def __init__(self, yearly_amount, years):
        self.yearly_amount = yearly_amount
        self.years = years
        self.balance = 0

    def calculate_growth(self):
        for year in range(1, self.years + 1):
            starting_value = self.balance
            after_deposit = starting_value + self.yearly_amount
            final_value = after_deposit * 1.10
            self.balance = final_value

            print(f"{year:4} | {starting_value:14.2f} | {self.yearly_amount:9.2f} | {final_value:20.2f}")

        print("\nFinal value of savings plan:", round(self.balance, 2))

amount = float(input("Enter yearly savings amount: "))
years = int(input("Enter number of years: "))

plan = SavingsPlan(amount, years)
plan.calculate_growth()