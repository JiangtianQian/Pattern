import csv

target = []

with open('combine.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        target.append(line[0])


with open('matchCombine.csv', 'w') as csvfile:
    fieldnames = ['ids', 'tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    with open('feature20.csv') as dfile:
            f_csv = csv.reader(dfile)
            for line in f_csv:
                if line[0] in target:
                    write_dict = {}
                    write_dict['ids'] = line[0]
                    write_dict['tag'] = line[2]
                    writer.writerow(write_dict)

        