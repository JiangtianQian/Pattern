import csv

b = []
write_dict = {}
with open('creator.csv') as fi:
    creat = csv.reader(fi)
    for r in creat:
        b.append(r[0])

count = 0
with open('r.csv', 'w') as csvfile:
    fieldnames = ['user_id', 'creator_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    with open('q.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            a = row
            count = count+ 1
            if (a['user_id'] in b) & (a['creator_id'] in b) & (a['user_id'] != a['creator_id']):               
                write_dict['user_id']= row['user_id']
                write_dict["creator_id"] = row['creator_id']
                writer.writerow(write_dict)
    
print "done"



