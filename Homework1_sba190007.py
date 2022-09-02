# CS4395.001 Portfolio Assignment 1: Text Processing with Python
# Shane Arwood
# September 4, 2022
# Dr. Karen Mazidi
"""
This program reads in a file containing employee records (full name, phone, and employee id).
It processes the text in the file and converts it to a standardized format, then pickles it,
unpickles it, and displayed the formatted data for each person. It has a method to read and
process the initial text and a Person class with a display method.
"""

import sys
import pathlib
import re
import pickle


# Person class which sets the employee's name, id, and phone. It contains a display method to
# output the formatted person information.
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print('\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t' + self.phone)


# Function that opens the data file given the file path and reads the file
# line by line. Employee information is parsed and formatted then a Person
# object is created and added to a dictionary. The dictionary is returned.
def process_text(filepath):
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as data_file:
        next(data_file)  # skip first line in data file

        # declare dictionary for person objects
        employee_dictionary = {}

        # process data line by line (person by person)
        for line in data_file:
            text_variables = line.split(',')

            # modify first and last name to be capitalized
            text_variables[0] = text_variables[0].capitalize()
            text_variables[1] = text_variables[1].capitalize()

            # modify middle initial to be single uppercase letter, or X if not given
            if text_variables[2].islower():
                text_variables[2] = text_variables[2].capitalize()
            if not text_variables[2]:
                text_variables[2] = 'X'

            # modify id to be 2 letters followed by 4 digits
            valid_id = re.match('[A-Z][A-Z][0-9]{4}', text_variables[3])
            while not valid_id:
                print('ID invalid: ' + text_variables[3])
                print('ID is two letters followed by 4 digits')
                print('Please enter a valid id: ')
                text_variables[3] = input()
                valid_id = re.match('[A-Z][A-Z][0-9]{4}', text_variables[3])

            # modify phone number to be in form 999-999-999
            valid_phone = re.match('[0-9]{3}-[0-9]{3}-[0-9]{4}', text_variables[4])
            while not valid_phone:
                print('Phone ' + text_variables[4].strip() + " is invalid")
                print('Enter phone number in form 123-456-7890')
                print('Enter phone number: ')
                text_variables[4] = input()
                valid_phone = re.match('[0-9]{3}-[0-9]{3}-[0-9]{4}', text_variables[4])

            # create person object
            employee = Person(text_variables[0], text_variables[1], text_variables[2], text_variables[3],
                              text_variables[4])

            # check id doesn't already exist in the dictionary, then add person object
            repeat = False
            for key in employee_dictionary:
                if key == text_variables[3]:
                    print('Error: Repeat ID found.')
                    repeat = True
                    break

            if not repeat:
                employee_dictionary[text_variables[3]] = employee

    return employee_dictionary


# Main, which checks that the user has provided a sysarg containing the file path.
# If the path is provided, the process_text function is called and the returned
# dictionary is saved as a pickle file. The file is then unpickled, read, and
# the data for each employee is displayed.
if __name__ == '__main__':
    # ensure path to data file has been provided
    if len(sys.argv) < 2:
        print('Please enter the relative path to data.csv in a sysarg.')
        sys.exit()
    else:
        # create pickle file with processed text
        file_path = sys.argv[1]
        pickle.dump(process_text(file_path), open('data_dictionary.p', 'wb'))

        # unpickle and display the data
        print('Employee list:\n')
        pickle_dictionary = pickle.load(open('data_dictionary.p', 'rb'))

        for key in pickle_dictionary:
            print('Employee id: ' + key)
            pickle_dictionary[key].display()
