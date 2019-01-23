# This module contains the class Account, which is used by the banking
# system in the file 'bank.py'.

class Account:

    def __init__(self, owner, acc_num, initial_depo):
        self._owner_name = owner
        self._balance = float(initial_depo)
        print(f'\n\tHello {owner}\n'
              f'\tThe account number of your new savings account is '
              f'{acc_num}\n'
              f'\tThe initial balance of that account was set to '
              f'{initial_depo}')

    def _correct_owner(self, owner, acc_num):
        if self._owner_name != owner:
            print(f'\n\t{owner} is not the correct owner of '
                  f'the account {acc_num}.')
            return False
        return True

    def _balance_ok(self, withdrawal_amount):
        return self._balance >= float(withdrawal_amount)

    def show_balance(self, owner, acc_num):
        if not self._correct_owner(owner, acc_num):
            print(f'\tUnable to display the account balance.')
        else:
            print(f'\n\tThe current balance of the account {acc_num} is '
                  f'{self._balance}')

    def deposit(self, owner, acc_num, depo_amount):
        if not self._correct_owner(owner, acc_num):
            print(f'\tUnable to make the requested deposit.')
        else:
            self._balance += float(depo_amount)
            print(f'\n\tDeposited {depo_amount}. ')
            print(f'\tThe new balance of the account {acc_num} is '
                  f'{self._balance}')

    def withdraw(self, owner, acc_num, wd_amount):
        if not self._correct_owner(owner, acc_num):
            print(f'\tUnable to make the requested withdrawal.')
        elif not self._balance_ok(wd_amount):
            print(f'\n\tUnable to withdraw {wd_amount} from the current '
                  f'balance of {self._balance}.')
        else:
            self._balance -= float(wd_amount)
            print(f'\n\tWithdrew {wd_amount}. ')
            print(f'The new balance of the account {acc_num} is '
                  f'{self._balance}')
            

