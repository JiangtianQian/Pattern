import csv

target = {}
flag = 'True'
with open('tags.csv') as tfile:
    f_csv = csv.reader(tfile)
    for line in f_csv:
        tmp = []
        tmp = line[0][1:len(line[0])-1].split(', ')
        for i in range(len(tmp)):
            if len(tmp[i]) != 0:
                n = tmp[i][1:len(tmp[i]) - 1]
                if target.has_key(n):
                    flag = 'false'
                    target[n] = target[n] + 1
                    out = target[n]
                else:
                    target[n] =  1


with open('tags40.csv', 'w') as csvfile:
    fieldnames = ['tags', 'num']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in target:
        write_dict = {}
        write_dict['tags']= i
        write_dict['num'] = target[i]
        writer.writerow(write_dict)
        
print "done"