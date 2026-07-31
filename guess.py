import sqlite3
import pandas as pd

print('What is the type of above given database - \n 1) Relational Database \n 2)Non-Relational Database')
answer = int(input('Enter your guess here... '))
if answer == 2:
    print('You guessed it right')
else:
    print('Unfortunately you guess was wrong')

print('\nPlease tell you mentor why you guessed this')