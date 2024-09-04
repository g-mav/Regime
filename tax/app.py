from flask import Flask, request, render_template
import tax

app = Flask(__name__)

def format_amount(amount):
    # Convert amount to a string with 2 decimal places
    amount_str = f"{amount:,.2f}"
    
    # Split into integer and decimal parts
    integer_part, decimal_part = amount_str.split('.')
    
    # Remove existing commas for proper processing
    integer_part = integer_part.replace(',', '')

    # Handle Indian numbering format
    if len(integer_part) <= 3:
        formatted_integer = integer_part
    else:
        # Reverse integer part for easier processing
        integer_part = integer_part[::-1]
        # Add commas for thousands, lakhs, and crores
        formatted_integer = integer_part[:3] + ',' + ','.join([integer_part[i:i+2] for i in range(3, len(integer_part), 2)])
        # Reverse it back
        formatted_integer = formatted_integer[::-1]
    
    return f"{formatted_integer}.{decimal_part}"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    income = request.form["income"]
    deductions = request.form["deduction"]
    old_tax, new_tax = tax.compare_and_calculate(int(income), int(deductions))
    
    if new_tax < old_tax:
        choose = 'New Tax Regime'
        benefit = old_tax - new_tax
        savings_message = f"You save approximately ₹{format_amount(benefit)} by choosing the new tax regime."
    else:
        choose = 'Old Tax Regime'
        benefit = new_tax - old_tax
        savings_message = f"You save approximately ₹{format_amount(benefit)} by choosing the old tax regime."

    # Format the results
    old_tax = format_amount(old_tax)
    new_tax = format_amount(new_tax)
    benefit = format_amount(benefit)

    return render_template("index.html", ot=old_tax, nt=new_tax, benefit=benefit, regime=choose, message=savings_message)

if __name__ == '__main__':
    app.run(debug=True, port=8000)