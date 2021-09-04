import pandas as pd
import csv
from datetime import datetime as dt,timedelta
#import sendmail
from openpyxl import Workbook, load_workbook

#read excel
read_file = pd.read_excel('DMM Access cards details.xlsx')

#convert into csv
read_file.to_csv('DMM Access cards details.csv',index=None,header=True)

#Excel for filtered data
wb = Workbook()
ws = wb.active
ws.title = "Data"

#filtering data
with open('DMM Access cards details.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Add header for Excel
    header = next(csv_reader)
    ws.append(header)

    #removing header
    next(csv_reader,None)

    #reminding days before expired
    remind_day = dt.now().date() - timedelta(days = 5)
    #remind_cards = []

    for row in csv_reader:
        if dt.strptime(row[5],'%Y-%m-%d').date() == remind_day:
            #remind_cards.append(row[2])
            #Adding filterd data
            ws.append(row)
            
    #Save filtered data
    wb.save('Reminder_VehicleCard_Data.xlsx')
    







    #sending mail
    #sendmail.remindcards(remind_cards)
    


