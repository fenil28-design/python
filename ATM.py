def manu ():
   print("\nATM menu:")
   print("1.cheak balance:")
   print("2.deposit money:")
   print("withdraw money:")
   print("4.exit:")

def cheak_balance(balance):
        print(f"your current balance is: ${balance.2f}")

def deposit_money(balance):
    amount = float(input("enter the amount to deposit: $"))
    if amount > 0:
         balance  += amount
             print(f"you have sucsefully deposited ${amount:.2f}.")
    else:
             print("invalid Amount.deposit failed.")
             return balance

             def withdraw_money(balance):
                   amount = float(input("Enter The amount to withdraw: $"))
                   if amount > 0:
                   if amount <= balance:
                         balance -= amount
                             print(f"you have succsesfully withdrawn ${amount:.2f}.")
                   else:
                             print("Insufficiant balannce.Withdrawal failed.")
                   else:
                             print("invalid amount.withdrawal failed.")
    return balance

    def main():
        balance =0.0
        while True:
            manu()
                choice = input("Enter your choice(1-4): ")
            if choice == '1':
                cheack_balance(balance)
                elif choice == '2':
                    balance = deposit_money(balance)
                elif choice == '3': 
                    balance = withdraw_money(balance)
                elif choice == '4':
                    print("Thank you for using the ATM.")
                    break
                else:
                    print("Invalid choice.please select a valid option.")

                    if__name__ == "__main__":
                       main()
                    

    
