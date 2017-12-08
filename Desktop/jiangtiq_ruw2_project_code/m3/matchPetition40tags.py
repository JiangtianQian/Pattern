import csv

tagList = []


with open('tags40noD.csv') as tfile:
    f_csv = csv.reader(tfile)
    for line in f_csv:
        tagList.append(line[0])
        
        


with open('newResultWith40TagwithoutD.csv', 'w') as csvfile:
    fieldnames = ['ids','discription','tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    with open('resultR.csv') as tfile:
        f_csv = csv.reader(tfile)
        for line in f_csv:
            flag = 'False'
            tmp = []
            if len(line[2]) != 0:
                tmp = line[2][1:len(line[2])-1].split(', ')
                newTag = []
                for i in range(len(tmp)):
                    if len(tmp[i]) != 0:
                        n = tmp[i][1:len(tmp[i]) - 1]
                        #print n
                        if n in tagList:
                            flag = 'True'
                            newTag.append(n)
                if flag == 'True':
                    write_dict = {}
                    write_dict['ids']= line[0]
                    write_dict['discription'] = line[1]
                    write_dict['tags'] = newTag
                    writer.writerow(write_dict)
        
print "done"
