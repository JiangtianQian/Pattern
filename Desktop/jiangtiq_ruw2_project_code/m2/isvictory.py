import csv
import json
import re

file1 = open('result.txt')
idstore = []
with open('isvictory.csv', 'w') as csvfile:
    fieldnames = ['petition_id', 'is_victory']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while 1:
        line = file1.readline()
        if not line:
            break
        if line != '\r\n':
            tmp = {}
            tag = []
            e = eval(str(line))
            c = json.dumps(e)
            d = json.loads(c)
            write_dict = {}
            p_id = d["petition_id"]
            if p_id in idstore:
                continue
            write_dict['petition_id']= p_id
            write_dict['is_victory'] = d['petition']
            writer.writerow(write_dict)
            idstore.append(p_id)
           
file1.close()
print "done"



