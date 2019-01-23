# This module contains the class Account, which is used by the banking
# system in the file 'bank.py'.

class Account:

    def __init__(self, owner_name, initial_deposit):
        self.owner_name = owner_name
        self.balance = float(initial_deposit)

    def _correct_owner(self, owner_name):
        return self.owner == owner_name

    def _balance_ok(self, withdrawal_amount):
        return self.balance >= float(withdrawal_amount)

            
            

