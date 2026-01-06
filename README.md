# -Electricity-Bill-Program
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = 0
elif units > 100 and units < 200:
    bill = (units - 100) * 5
elif units>=201 and units<=300:
    bill=(units - 201) * 7
elif units>=301 and units<=500:
    bill=(units - 301) *10
else:
    bill = (100*5)+(100*7)+(units-300)*10

print("Electricity Bill:", bill)
