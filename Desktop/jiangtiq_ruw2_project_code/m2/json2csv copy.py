import csv
import json
import re

file1 = open('result.txt')
idstore = []
with open('resultR5.csv', 'w') as csvfile:
    fieldnames = ['petition_id', 'discription','tag']
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
            dis = d["petition_text"]
            p = re.compile(r'<.*?>')
            dis = p.sub('',dis)
            p = re.compile(r'[^a-zA-z]')
            discription = p.sub(' ',dis)
            discription = re.sub(r'\s+', ' ', discription)
            
            stoplist = set('i she [ ] him no else now years year you also i m I am who had been who still me unless z but didn t all isn an how amp been upon an one two three four most does its does did done was she he his her if do did us would could should may must not it have has just we our will they their many more much less about into out without according apart from including concerning outside by month year since each only because toward so till until or and at before after next last previous however for with within be x b c d e as something it by a of up off down here there the and to in into on from another this that which where why our my is were are those these am what'.split())
            texts = [word.encode('utf-8') for word in discription.lower().split() if word not in stoplist]

            write_dict["discription"] = texts
            tmp = d["tags"]
            for i in range(len(tmp)):
                tag.append(tmp[i]['name'].encode('utf-8'))
            write_dict["tag"] = tag
            writer.writerow(write_dict)
            idstore.append(p_id)
           
file1.close()
print "done"



