import csv

target = {}
result = {}
with open('resultR.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        target[line[0]] = line[2]
        arr = line[2][1:len(line[2])-1].split(', ')
        for i in range(len(arr)):
            if len(arr[i]) != 0:
                result[arr[i]] = 0
                
with open('isvictory.csv') as vfile:
    f_csv = csv.reader(vfile)
    for line1 in f_csv:
        if target.has_key(line1[0]):
            arr1 = target[line1[0]][1:len(line[2])-1].split(', ')
            for i in range(len(arr1)):
                if line1[1] == 'TRUE':
                    if result.has_key(arr1[i]):
                        result[arr1[i]] = result[arr1[i]] + 1

with open('tu.csv', 'w') as csvfile:
    fieldnames = ['tags', 'num']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in result:
        write_dict = {}
        write_dict['tags']= i
        write_dict['num'] = result[i]
        writer.writerow(write_dict)
        
print "done"