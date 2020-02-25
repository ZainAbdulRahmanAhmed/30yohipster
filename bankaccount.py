# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:44:03 2020

@author: zain AR ahmed
"""

class BankAccount(object):
    
    def __init__(self, balance=0.0):
        self.balance = balance
        
    def deposit(self):
        d = float(input('How much money do you want to deposit? > '))
        self.balance += d
        print(f'You deposited ${round(d, 2):.2f}.')
    
    def withdraw(self):
        w = float(input('How much money do you want to withdraw? > '))
        if w > self.balance:
            print(f'Insufficient funds. Your balance is ${round(self.balance, 2):.2f}.')
        else:
            self.balance -= w
            print(f'You withdrew ${round(w, 2):.2f}.')
    
    def display_balance(self):
        print(f'Your balance is ${round(self.balance, 2):.2f}. ')

fifth_third = BankAccount()
print('''
Welcome to your bank account! 
Type a number to perform the action. 
------------------------------------ 
1. Display balance
2. Deposit
3. Withdraw
4. Exit''')

while True:
    action = input('> ')
    if action == '1':
        fifth_third.display_balance()
    elif action == '2':
        fifth_third.deposit()
    elif action == '3':
        fifth_third.withdraw()
    elif action == '4':
        print('Goodbye.')
        break
    else:
        print('Please type a number.')
