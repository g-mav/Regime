class OldRegime:
    def __init__(self, income):
        self.income = income
        self.tax = 0

    def calculate_tax(self):
        if self.income <= 500000:
            return 0
        elif self.income <= 1000000:
            return (self.income - 250000) * 0.05
        elif self.income <= 1000000:
            return (500000 - 250000) * 0.05 + (self.income - 500000) * 0.20
        else:
            return (500000 - 250000) * 0.05 + (1000000 - 500000) * 0.20 + (self.income - 1000000) * 0.30

    def calculate_cess(self):
        return self.calculate_tax() * 1.04    

class NewRegime:
    def __init__(self, income):
        self.income = income
        self.tax = 0

    def calculate_tax(self):
        if self.income <= 300000:
            return 0
        elif self.income <= 600000:
            return (self.income - 300000) * 0.05
        elif self.income <= 900000:
            return (600000 - 300000) * 0.05 + (self.income - 600000) * 0.10
        elif self.income <= 1200000:
            return (600000 - 300000) * 0.05 + (900000 - 600000) * 0.10 + (self.income - 900000) * 0.15
        elif self.income <= 1500000:
            return (600000 - 300000) * 0.05 + (900000 - 600000) * 0.10 + (1200000 - 900000) * 0.15 + (self.income - 1200000) * 0.20
        else:
            return (600000 - 300000) * 0.05 + (900000 - 600000) * 0.10 + (1200000 - 900000) * 0.15 + (1500000 - 1200000) * 0.20 + (self.income - 1500000) * 0.30

    def calculate_cess(self):
        return self.calculate_tax() * 1.04    

def compare_and_calculate(income, deduction):
    taxable_income_old = income - deduction - 50000
    taxable_income_new = income - 50000

    # Old Regime
    OR = OldRegime(taxable_income_old)
    old_tax = OR.calculate_cess()  

    # New Regime
    NR = NewRegime(taxable_income_new)
    new_tax = NR.calculate_cess()

    return old_tax, new_tax

def human_round(number):
    if number < 1000:
        return round(number, -1)  # Round to nearest 10
    elif number < 100000:
        return round(number, -3)  # Round to nearest 1000
    elif number < 10000000:
        return round(number, -4)  # Round to nearest 10000
    else:
        return round(number, -5)  # Round to nearest 100000

if __name__ == "__main__":
    income = int(input("Enter your Income: "))            
    deduction = int(input("Enter your Deduction: "))     

    old_tax, new_tax = compare_and_calculate(income, deduction)

    old_tax_rounded = human_round(old_tax)
    new_tax_rounded = human_round(new_tax)
    
    print(f"Old Tax = {old_tax_rounded}")
    print(f"New Tax = {new_tax_rounded}")
    
    if new_tax_rounded < old_tax_rounded:
        print(f"Choose New Tax Regime")
        print(f"Benefit: {old_tax_rounded - new_tax_rounded}")  
    else:
        print(f"Choose Old Tax Regime")
        print(f"Benefit: {new_tax_rounded - old_tax_rounded}") 