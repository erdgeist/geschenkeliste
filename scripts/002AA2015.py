# coding=utf-8
import csv
import re
oldRow = ['gift', 'Auswärtiges Amt','2013', 'n.a.', 'n.a.', 'AA', 'n.a.']
newRow = ['gift', 'year', 'month', 'day', '00.00', 'false', 'false', 'fate', 'n.a.', 'AA']

aa13 =  open('../data/csvNewModel/aa15.csv', 'w')



with open('/Users/krawallmietze/code/python/geschenkeliste/data/csvTxtPreprocess/2015AA.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        if len(row) >3:
            if row[2] != '': #filters out empty rows
                #delete newline chars
                #oldRow = row
                #row = []

                row = [re.sub(r'(\r\n|\n|\r)', ' ', el) for el in row]

                # for el in oldRow:
                #     el = re.sub(r'(\n|\r)', ' ', el)
                #     row.append(el)
                #     print(el)
                    #el = el.replace('\n', '')

                #get date
                if row[0] == '':
                    newRow[1] = '2015'
                    newRow[2] = '00'
                    newRow[3] = '00'
                else:
                    datetemp = row[0]
                    datelist = datetemp.split('.')
                    if len(datelist) == 3:
                        newRow[1] = datelist[2]
                        newRow[2] = datelist[1]
                        newRow[3] = datelist[0]
                    elif((len(datelist) == 1) & (datelist[0] != '???')):
                        newRow[1] = datelist[0]

                #get gift
                if ',' not in row[2]:
                    newRow[0] = row[2]
                    if row[1] not in ['', 'Zentrale']:
                        given = ' An: ' + row[1]
                        newRow[0] += given
                else:
                    newRow[0] = '"' + row[2]
                    if row[1] not in ['', 'Zentrale']:
                        given = ' An: ' + row[1]
                        newRow[0] += given + '"'
                    else:
                        newRow[0] += '"'
                #get fate + success
                if row[-1] != '':
                    newRow[7] = row[-1]
                    newRow[8] = 'fail'
                    if 'BM' in row[-1]:
                        newRow[8] = 'success'

                #get price
                if row[3] != '':
                 print row[3]

                #print newRow
                aa13.write(', '.join(newRow) + '\n')
