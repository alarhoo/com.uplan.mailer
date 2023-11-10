# This is final working peice
import csv
import os
from datetime import datetime
from sendBirthdayEmail import sendBirthdayEmail
from sendAnniversaryEmail import sendAnniversaryEmail
import traceback
import logging


def isToday(dob):
    # Returns True if Birthday/Anniversary is Today else False
    today = datetime.today().date()
    return dob.month == today.month and dob.day == today.day


def ParseCSV():
    # Parse EmployeesMain.csv and check if anyone has a Birthday today
    data_dir = os.getcwd() + "\\data\\"
    filename = data_dir + "EmployeesMain.csv"
    data = []
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            # header = next(csvreader)
            for row in csvreader:
                emp_main_dob = datetime.strptime(row[4], '%Y-%m-%d').date()
                emp_main_doj = datetime.strptime(row[14], '%Y-%m-%d').date()
                emp_main_active = int(row[16])
                # Check if anyone has birthday Today()
                if(isToday(emp_main_dob) and emp_main_active):
                    emp_main_first = row[1]
                    emp_main_last = row[3]
                    emp_main_gender = int(row[5])
                    emp_main_email = row[7]
                    emp_main_designation = row[9]
                    data.append([emp_main_first, emp_main_last, emp_main_dob,
                                 emp_main_gender, emp_main_email, emp_main_designation])
                    sendBirthdayEmail(emp_main_first, emp_main_last, emp_main_dob,
                                      emp_main_gender, emp_main_email, emp_main_designation)
                # Check if anyone has anniversay Today()
                if(isToday(emp_main_doj) and emp_main_active):
                    emp_main_first = row[1]
                    emp_main_last = row[3]
                    emp_main_gender = int(row[5])
                    emp_main_email = row[7]
                    emp_main_designation = row[9]
                    data.append([emp_main_first, emp_main_last,
                                 emp_main_gender, emp_main_email, emp_main_designation, emp_main_doj])
                    sendAnniversaryEmail(emp_main_first, emp_main_last, emp_main_gender,
                                         emp_main_email, emp_main_designation, emp_main_doj)
        print(data)
    except Exception as e:
        logging.error("Something went wrong while parsing!" + str(e))
        logging.error(traceback.format_exc())


ParseCSV()
