hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

if h < 40:
    pay = h * r
    print("Pay:", str(pay))

else:
    pay = ((h - 40) * (r * 1.5)) + (40 * r)
    print("Pay:", str(pay))
