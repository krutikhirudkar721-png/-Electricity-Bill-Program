# -Electricity-Bill-Program
# Logic: 1-100 (Free), 101-200 (5/unit), 201-300 (7/unit), 300+ (10/unit)
# BASIC


units = int(input("Enter electricity units consumed: "))
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
elif units <= 300:
    bill = (100 * 5) + (units - 200) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 300) * 10

print("Total Bill: ₹", bill)

# Advance

    def calculate_electricity_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative.")
    bill = 0

    if units > 300:
        bill += (units - 300) * 10
        units = 300

    if units > 200:
        bill += (units - 200) * 7
        units = 200

    if units > 100:
        bill += (units - 100) * 5

    return bill
try:
    units = int(input("Enter electricity units consumed: "))
    total_bill = calculate_electricity_bill(units)

    print("\n--- Billing Summary ---")
    print("Units Consumed:", units)
    print(f"Total Amount: ₹{total_bill:.2f}")

except ValueError as e:
    print("Error:", e)
