import csv
import re

d = {}


with open('resultR.csv') as tfile:
    f_csv = csv.reader(tfile)
    for line in f_csv:
        if line[0].isdigit():
            d[line[0]] = line[1]
                  
with open('vic_des.csv', 'w') as csvfile:
    fieldnames = ['id','description','victory']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    with open('isvictory.csv') as tfile:
        f_csv = csv.reader(tfile)
        for row in f_csv:
            if d.has_key(row[0]):
                write_dict = {}
                write_dict['id'] = row[0]
                write_dict['description'] = d[row[0]]
                write_dict['victory'] = row[1]
                writer.writerow(write_dict)
                
      
print "done"
