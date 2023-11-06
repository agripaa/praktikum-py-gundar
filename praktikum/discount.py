def main():
    price = 990000
    amount = int(input('Masukkan banyak pembelian: '))
    
    discount, total_disc = calculate_discount(amount, price)
    
    if discount > 0:
        print(f'Diskon = Rp.{discount:,.2f}')
    
    print(f'Total = Rp.{total_disc:,.2f}')

def calculate_discount(amount, price):
    total = amount * price
    discount_percentage = 0

    if amount >= 10 and amount <= 19:
        discount_percentage = 0.2
    elif amount >= 20 and amount <= 49:
        discount_percentage = 0.3
    elif amount >= 50 and amount <= 99:
        discount_percentage = 0.4
    elif amount >= 100:
        discount_percentage = 0.5

    discount = total * discount_percentage
    total_disc = total - discount

    return discount, total_disc

main()