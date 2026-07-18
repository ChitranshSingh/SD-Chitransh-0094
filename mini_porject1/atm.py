# ATM Withdrawal Program

print("========== ATM MACHINE ==========")

# Input account balance
acc_no = float(input("Enter your five digit account Number: "))

# Input withdrawal amount
withdraw = float(input("Enter the amount to withdraw: ₹"))

# Check withdrawal conditions
if withdraw <= 0:
    print("Invalid withdrawal amount.")

elif withdraw > balance:
    print("Transaction Failed!")
    print("Insufficient balance.")

else:
    balance -= withdraw
    print("\nTransaction Successful!")
    print(f"Please collect your cash: ₹{withdraw}")
    print(f"Remaining Balance: ₹{balance:.2f}")

print("\nThank you for using our ATM.")