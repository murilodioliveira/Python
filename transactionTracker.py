def after_transaction(balance, transaction):
    checkTransaction = balance + transaction
    if (checkTransaction) < 0:
        print("No limit in account. Transaction ignored.")
        print(f"Your balance is: {balance}")
    else:
        balance = balance + transaction
        print(f"Your balance is now: {balance}")
        
        
after_transaction(500,20)
after_transaction(300,-200)
after_transaction(3,-1000)
after_transaction(3,-4)
after_transaction(3,-3)