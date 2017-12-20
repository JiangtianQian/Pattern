import csv
import json
import re






tags = []


with open('tags.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        tmp = line[0][1:len(line[0]) - 1]
        p = re.compile(r"'")
        tmp = p.sub('',tmp)
        p = re.compile(r'"')
        tmp = p.sub('',tmp)
        tmp = tmp.split(', ')
        a = []
        for word in tmp:
            if len(word) != 0:
                if word[0].isupper():
                    a.append(word)
        tags.append(a)


with open('tagsNew.csv', 'w') as csvfile:
    fieldnames = ['tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(tags)):
        write_dict = {}
        write_dict["tags"] = tags[i]
        writer.writerow(write_dict)
    
    
   
print "done"