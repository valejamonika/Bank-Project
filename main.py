from bank_account import BankAccount
from atm_card import AtmCard
from loan_account import Loan_Account


def is_valid_aadhar(aadhar):
    return len(aadhar) == 12 and aadhar.isdigit()


def get_valid_aadhar(aadhar):
    while not is_valid_aadhar(aadhar):
        print("Please enter a valid Aadhar card number.")
        aadhar = input("Aadhar Card No: ")
    return aadhar


def is_valid_pan(pan):
    return (
        len(pan) == 10
        and pan[:5].isalpha()
        and pan[5:9].isdigit()
        and pan[9].isalpha()
    )


def get_valid_pan(pan):
    while not is_valid_pan(pan):
        print("Please enter a valid PAN card number.")
        pan = input("PAN Card No: ")
    return pan

# creating object of class BankAccount, AtmCard, Loan_Account


obj = BankAccount()
abj = AtmCard()
lbj = Loan_Account()

# Driver Program Section

while True:
    q = str(input("Press Q for quit or Any key to continue")).upper()
    if q == "Q":
        print("Thanks for using using this program...!!!!!")
    else:
        choose = int(input("""
                    Press 1 for ----Open Account----\n
                    Press 2 for ----Cash Deposite----\n
                    Press 3 for ----Cash Withdraw----\n
                    Press 4 for ----Balance Check----\n
                    Press 5 for ----For Getting ATM Card----\n
                    Press 6 for ----Check Atomated Generated Pin For ATM----\n
                    Press 7 for ----For Changing ATM Pin----\n
                    Press 8 for ----Cash Withdraw From ATM----\n
                    Press 9 for ----Apply For Loan----\n
                    Press 10 for ----Apply Depositing EMI----\n
                    Press 11 for ----For Check Outstanding Balance----\n\n
                    Press 12 for ----For Get Statement----\n\n
                    Please Enter Your Choice: """))
    if choose == 1:
        name = input("Enter Your Name: ")
        adhar_card = input("Enter Adhar Card Number: ")
        adhar = get_valid_aadhar(adhar_card)
        pancard_no = input("Enter Pancard Card No: ")
        pan_no = get_valid_pan(pancard_no)
        address = input("Enter Address: ")
        photo = input("Add a link to your photo: ")
        user_input = {
            "name": name,
            "adhar_number": adhar,
            "pan_card": pan_no,
            "address": address,
            "photo": photo
            }
        obj.open_account(user_input)
    elif choose == 2:
        account_no = str(input("Please Enter Account No Of Account Holder:"))
        amount = float(input("How Much Amount Do You Want To Deposite:"))
        obj.deposit_cash(account_no, amount)
    elif choose == 3:
        account_no = input("Please Enter Account No Of Account Holder: ")
        amount = float(input("How Much Amount Do You Want To Withdraw: "))
        obj.withdraw_cash(account_no, amount)
    elif choose == 4:
        account_no = str(input("Please enter your account no:"))
        obj.check_balance(account_no)
    elif choose == 5:
        account_no = str(input("Please enter your account no:"))
        abj.show_atm_card_no(account_no)
    elif choose == 6:
        account_no = str(input("Please enter your account no:"))
        atm_card_no = str(input("Enter Your ATM Card Number:"))
        abj.pin_data(account_no, atm_card_no)
    elif choose == 7:
        atm_card_no = str(input("Enter Your ATM Card Number:"))
        old_pin = int(input("Enter Your old pin:"))
        abj.gen_new_pin(atm_card_no, old_pin)
    elif choose == 8:
        atm_card_no = str(input("Enter Your ATM Card Number:"))
        pin = str(input("Enter your atm pin:"))
        abj.atm_withdraw(atm_card_no, pin)
    elif choose == 9:
        account_no = str(input("Please enter your account no:"))
        lbj.open_loan_account(account_no)
    elif choose == 10:
        loan_account_no = int(input("Please enter your loan account no:"))
        lbj.deposite_emi(loan_account_no)
    elif choose == 11:
        loan_account_no = int(input("Please enter your loan account no:"))
        lbj.outstanding_balance(loan_account_no)
    elif choose == 12:
        account_no = str(input("Please enter your account no:"))
        obj.statement(account_no, print_statement=True)
    else:
        print("Please Enter Correct Option !!!")

# End of driver program
