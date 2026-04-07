# -Electricity-Bill-Program
# Logic: 1-100 (Free), 101-200 (5/unit), 201-300 (7/unit), 300+ (10/unit)

# BASIC
    units = int(input("Enter electricity units consumed: "))
    <br>
    if units <= 100:
    bill = 0
    <br>
    elif units <= 200:
    bill = (units - 100) * 5
    <br>
    elif units <= 300:
    bill = (100 * 5) + (units - 200) * 7
    <br>
    else:
    bill = (100 * 5) + (100 * 7) + (units - 300) * 10
    <br>
    print(f"Total Electricity Bill: {bill}")

# Advance
    def calculate_electricity_bill(units: int) -> float:
    """
    Calculates cumulative electricity bill based on unit slabs.
    Slabs:
    - 0 to 100 units: Free
    - 101 to 200 units: 5/unit
    - 201 to 300 units: 7/unit
    - Above 300 units: 10/unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")
    bill = 0.0
    if units <= 100:
        bill = 0.0
    elif units <= 200:
        bill = (units - 100) * 5
    elif units <= 300:
        # 100 units at 0 + 100 units at 5 + current slab
        bill = (100 * 5) + (units - 200) * 7
    else:
        # 100 units at 0 + 100 units at 5 + 100 units at 7 + current slab
        bill = (100 * 5) + (100 * 7) + (units - 300) * 10
    return bill
    def main():
    try:
        units_input = input("Enter electricity units consumed: ")
        units = int(units_input)
        total_bill = calculate_electricity_bill(units)
        print(f"\n--- Billing Summary ---")
        print(f"Units Consumed: {units}")
        print(f"Total Amount:  Rs. {total_bill:.2f}")
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
    if __name__ == "__main__":
    main()

