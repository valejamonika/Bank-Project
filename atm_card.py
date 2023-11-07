import random
from datetime import date, timedelta
from bank_account import BankAccount


"""AtmCard class inherits BankAccount class and
    it responsible for issueing ATM card, for generating atomated ATM pin, for generating new pin and
    for withdrawing cash from ATM """


class AtmCard(BankAccount):
    def generate_card_no(self):
        card_number = "4"
        for _ in range(15):
            card_number += str(random.randint(0, 9))
        return card_number

    def generate_cvv(self):
        return random.randint(100, 999)

    def atm_card_issue(self, a_no):
        self.a_no = a_no
        self.card_no = self.generate_card_no()
        current_date = date.today()
        self.issue_date = str(current_date)
        self.expire_date = str(current_date + timedelta(days=365*5))
        self.users_cvv = self.generate_cvv()
        customer = self.search_customer(a_no)
        self.holder_data[self.holder_data.index(customer)]["ATM"] = {
            "ATM_card_no": self.card_no,
            "issue_date": self.issue_date,
            "expire_date": self.expire_date,
            "cvv": self.users_cvv
        }
        self.write_data()
        return self.search_customer(a_no)

    def show_atm_card_no(self, a_no):
        holder_data = self.read_data()
        for k in holder_data:
            if k.get('account_no') == a_no and 'ATM' in k and 'ATM_card_no' in k['ATM']:
                a = k['ATM']['ATM_card_no']
                return print("ATM Card Is Already Generated.!! ATM Card No - ", a)
        else:
            customer = self.atm_card_issue(a_no)
            print(customer)

    def generate_atomated_pin(self, a_no=None, atm_no=None):
        customer = self.search_customer(a_no)
        if customer["ATM"]["ATM_card_no"] == atm_no:
            pin = random.randint(1000, 9999)
            self.holder_data[self.holder_data.index(customer)]["ATM"]["pin"] = pin
            self.write_data()
            return print("Automated Generated ATM Pin For ATM Card No", atm_no, "Is", pin)
        else:
            return print("Unable To Generate Pin.. ATM Card No.Doesn't Match.. Please Try Again...!")

    def pin_data(self, a_no=None, atm_no=None):
        holder_data = self.read_data()
        for k in holder_data:
            if k.get('account_no') == a_no and k['ATM'].get('ATM_card_no') == atm_no and 'pin' in k['ATM']:
                p = k['ATM']['pin']
                return print("Automated Generated ATM Pin For ATM Card No", atm_no, "Is", p)
        else:
            self.generate_atomated_pin(a_no, atm_no)

    def gen_new_pin(self, atm_no=None, old_pin=None):
        holder_data = self.read_data()
        for k in holder_data:
            if 'ATM' in k and 'ATM_card_no' in k['ATM'] and 'pin' in k['ATM']:
                if k['ATM']['ATM_card_no'] == atm_no and k['ATM']['pin'] == old_pin:
                    new_pin = input("Enter Your New Pin: ")
                    re_enter = input("Re-Enter Your New Pin: ")
                    if new_pin == re_enter:
                        self.holder_data[self.holder_data.index(k)]["ATM"]["pin"] = re_enter
                        self.write_data()
                        print("Your Pin Successfully Changes!!....")
                        break
                    else:
                        print("Pin mismatch")
                        break
        else:
            print("ATM Card Number And Old Pin not Matched!!! ")

    def atm_withdraw(self, atm_no=None, pin=None):
        holder_data = self.read_data()
        for k in holder_data:
            if 'ATM' in k and k['ATM']['ATM_card_no'] == atm_no and k['ATM']['pin'] == pin:
                amt = float(input("How much amount you want to withdraw?"))
                self.holder_data[self.holder_data.index(k)]["balance"] -= amt
                self.write_data()
                print("Amount", amt, "is debited from ATM No.-", atm_no)
                break
        else:
            print("Atm and Pin Does Not Matched!!!...")
