tax_rate = 0.06

def get_sales_tax(total):
    return round(total * tax_rate, 2)

def get_total_after_tax(total):
    tax = get_sales_tax(total)
    return round(total + tax, 2)