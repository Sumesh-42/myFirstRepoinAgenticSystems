# Bank Withdrawal Simulation
# Get user input
account_balance = int(input("Enter your account balance: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))
verification_status_input = input("Are you verified? (True/False) ")
verification_status = verification_status_input == "True"
# Check withdrawal conditions
if verification_status and withdrawal_amount <= account_balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
    
