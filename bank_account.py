import random
import json
from datetime import datetime
import pandas as pd


"""Bank Account class responsible for opening bank account,
    deposite cash, withdraw cash, checking bank balance
    and for creating bank statement"""


class BankAccount():
    def __init__(self):
        try:
            self.holder_data = self.read_data()
        except FileNotFoundError:
            self.holder_data = []

    def generate_account_number(self):
        self.prefix = "ACC"
        self.number = random.randint(1000, 90000)
        self.account_no = f"{self.prefix}__{self.number}"
        return self.account_no

    def write_data(self):
        with open("bank_data.json", "w") as json_file:
            json_file.write(json.dumps(self.holder_data))

    def read_data(self):
        with open("bank_data.json", "r") as file:
            r_data = json.load(file)
            return r_data

    def open_account(self, user_input):
        self.a_holder_name = user_input.get("name")
        self.a_holder_adhar = user_input.get("adhar_number")
        self.a_holder_pan = user_input.get("pan_card")
        self.a_holder_address = user_input.get("address")
        self.a_holder_photo = user_input.get("photo")
        self.account_no = self.generate_account_number()
        data_dict = {
            "name": self.a_holder_name,
            "adhar": self.a_holder_adhar,
            "pan_no": self.a_holder_pan,
            "address": self.a_holder_address,
            "photograph": self.a_holder_photo,
            "account_no": self.account_no,
            "balance": 0
        }
        self.holder_data.append(data_dict)
        self.write_data()
        print("Your Account Is Successfully Created !!!!, Your Account Number Is ", self.account_no)

    def search_customer(self, a_no=None):
        get_data = self.read_data()
        customer_record = None
        for customer in get_data:
            if a_no == customer['account_no']:
                customer_record = customer
                return customer_record
        return print("No record found for Account No.- ", a_no)

    def deposit_cash(self, a_no, amount):
        record = self.search_customer(a_no)
        if record:
            self.holder_data[self.holder_data.index(record)]["balance"] += amount
            self.write_data()
            print("Amount", amount, "is credited to Account No.-", a_no)
            now = datetime.now()
            t_time = now.strftime("%d/%m/%Y %H:%M:%S")
            transaction_data = {"type": "credit", "date": t_time, "amount": amount}
            self.statement(a_no, transaction_data)

    def withdraw_cash(self, a_no, amount):
        record = self.search_customer(a_no)
        if record:
            self.holder_data[self.holder_data.index(record)]["balance"] -= amount
            self.write_data()
            print("Amount", amount, "is debited from Account No.-", a_no)
            now = datetime.now()
            t_time = now.strftime("%d/%m/%Y %H:%M:%S")
            transaction_data = {"type": "debit", "date": t_time, "amount": amount}
            self.statement(a_no, transaction_data)

    def check_balance(self, a_no):
        record = self.search_customer(a_no)
        if record:
            holder_name = record['name']
            curr_bal = record['balance']
            print("Account Holder Name :", holder_name)
            print("Current Bank Balance of Account No.", a_no, "is ", curr_bal)

    def statement(self, account_no, transaction_data=None, print_statement=False):
        record = self.search_customer(account_no)
        if print_statement:
            data = self.holder_data[self.holder_data.index(record)].get("transaction")
            df = pd.DataFrame(data)
            print(df)
        else:
            if self.holder_data[self.holder_data.index(record)].get("transaction"):
                self.holder_data[self.holder_data.index(record)]["transaction"].append(transaction_data)
            else:
                self.holder_data[self.holder_data.index(record)]["transaction"] = [transaction_data]
            self.write_data()
