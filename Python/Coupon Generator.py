base = "www.sym.co.uk"
coupon = "signup/coupon"
discount = 35
amount = 7


for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons made")