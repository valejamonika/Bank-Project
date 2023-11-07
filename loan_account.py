import random
from bank_account import BankAccount
from datetime import datetime


"""Loan Account class inherits BankAccount class and
    it responsible for opening loan account,
    deposite loan EMI and
    checking outstanding balance"""


class Loan_Account(BankAccount):
    def open_loan_account(self, a_no=None):
        customer = self.search_customer(a_no)
        if customer:
            self.user_input_amount = float(input("Enter the Loan Amount: "))
            if customer["balance"] * 5 < self.user_input_amount:
                self.user_input_amount = self.user_input_amount * 0.75

        type_of_loan = int(input("""
        Enter the type of loan:
        1 Personal Loan
        2 Education Loan
        3 Home Loan
        4 Car Loan
        5 Gold Loan
        Enter option: """))

        # Set the ROI and total years based on the loan type
        loan_types = {
            1: {"roi": "16%", "total_years": 0.5},
            2: {"roi": "12%", "total_years": 7},
            3: {"roi": "7.72%", "total_years": 20},
            4: {"roi": "8%", "total_years": 8},
            5: {"roi": "8%", "total_years": 3}
        }
        if type_of_loan == 1:
            no_of_years = int(input("How many years for your personal loan?"))
            loan_types[1]["total_years"] = no_of_years
        loan_type_info = loan_types.get(type_of_loan)
        if not loan_type_info:
            return "Invalid loan type."

        roi = loan_type_info["roi"]
        total_year = loan_type_info["total_years"]

        # Calculate loan parameters
        amount = round(self.user_input_amount * (1 + eval(roi.strip('%')) / 100) ** total_year, 2)
        emi = round(amount / (12 * total_year), 2)

        # Generate a random loan account number
        loan_account_no = random.randint(10000000000, 99999999999)

        # Update the customer's data with loan details
        loan_data = {
            "loan_account_no": loan_account_no,
            "total_amount": self.user_input_amount,
            "emi": emi,
            "no_of_emi": total_year * 12,
            "roi": roi,
            "total_months": total_year * 12,
            "outstanding_balance": amount
        }
        loan_data_list = self.holder_data[self.holder_data.index(customer)].get("Loan_Account")
        if loan_data_list:
            loan_data_list.append(loan_data)
        else:
            # loan_data_list = [loan_data]
            self.holder_data[self.holder_data.index(customer)]["Loan_Account"] = [loan_data]
        self.write_data()
        print("Your Loan account Is Successfully Opened ! Loan Account No - ", loan_account_no)

    def search_loan_customer(self, loan_no=None):
        holder_data = self.read_data()
        for k in holder_data:
            if 'Loan_Account' in k:
                for loan in k['Loan_Account']:
                    if loan.get('loan_account_no') == loan_no:
                        return loan, k

    # def deposite_emi(self, loan_ac_no = None, account_no = None, amt_deposite = None):
    #     customer = self.search_customer(account_no)
    #     cust_loan_account = None
    #     custumer_data  = self.holder_data
    #     if customer:
    #         custumer_data = self.holder_data[self.holder_data.index(customer)]
    #         if customer.get("Loan_Account"):
    #             for loan_account in customer["Loan_Account"]:
    #                 if loan_account["loan_account_no"] == loan_ac_no:
    #                     cust_loan_account = loan_account
    #         if customer['balance'] >= amt_deposite:
    #             customer["balance"] -= amt_deposite
    #             customer["Loan_Account"][customer["Loan_Account"].index(cust_loan_account)]["outstanding_balance"] -= amt_deposite
    #         custumer_data = customer
    #     self.write_data()

    def deposite_emi(self, loan_ac_no=None):
        loan_customer, customer = self.search_loan_customer(loan_ac_no)
        amt_deposite = loan_customer['emi']
        if loan_customer:
            if customer['balance'] >= amt_deposite:
                customer["balance"] -= amt_deposite
                customer["Loan_Account"][customer["Loan_Account"].index(loan_customer)]["outstanding_balance"] -= amt_deposite
        old_cust1, old_cust2 = self.search_loan_customer(loan_ac_no)
        self.holder_data[self.holder_data.index(old_cust2)] = customer
        self.write_data()
        print("Your EMI Deposited..!!!")
        now = datetime.now()
        t_time = now.strftime("%d/%m/%Y %H:%M:%S")
        transaction_data = {"type": "EMI debit", "date": t_time, "amount": amt_deposite}
        self.statement(customer['account_no'], transaction_data)

    def outstanding_balance(self, loan_ac_no=None):
        loan_customer, customer = self.search_loan_customer(loan_ac_no)
        return print("Your loan account no.", loan_customer['loan_account_no'], "has", loan_customer['outstanding_balance'], "outstanding balance....")
