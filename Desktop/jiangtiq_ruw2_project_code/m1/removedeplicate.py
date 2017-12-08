import csv

key = []
value = []
write_dict = {}


count = 0
with open('r1.csv', 'w') as csvfile:
    fieldnames = ['user_id', 'creator_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    with open('a.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            write_dict[row['user_id']]= row['creator_id']


print "done"



