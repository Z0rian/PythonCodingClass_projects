# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:18:17 2020

@author: zorian
"""

list_of_digits = [2, 7, 1, 8, 2, 8]
list_of_digits.append(2)

class Person():
    
    # Initialize class with name and birthyear
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    
    # Define greeting function
    def greeting(self):
        return f'Hello {self.name}.'
    
    #define function that returns number of seconds on earth
    def seconds(self):
        import datetime
        current_time = datetime.datetime.now()
        current_year = current_time.year
        time = (current_year - self.birthyear)
        time = datetime.datetime.now() - self.birthyear *60*60*24*365.25
        return f'{self.name} has spent {time} seconds on Earth.'
    
        
    


# Create instance of Class Person
zorian = Person('Zorian', 2006)

# Show greeting
print(zorian.greeting())

#show seconds on Earth
print(zorian.seconds())

import datetime
current_time = datetime.datetime.now()
my_birthdate = datetime.datetime(2006, 11, 7)
