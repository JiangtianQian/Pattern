import csv
import json,types

file1 = open('result1.txt')
with open('student1.csv', 'w') as csvfile:
	fieldnames = ['user_id', 'creator_id','type','weight','country','state','city']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	while 1:
		line = file1.readline()
		if not line:
			break
		if line != '\r\n':
			e = eval(str(line))
			c = json.dumps(e)
			d = json.loads(c)
			write_dict = {}
			write_dict['user_id']= d['user_id']
			write_dict["creator_id"] = d['creator']
			write_dict["type"] = "directed"
			write_dict["weight"] = 1
			write_dict["country"] = d['country_code']
			write_dict["state"] = d['state_code']
			a = d['city']
			if a is not None:
				write_dict["city"] = a.encode("utf-8")
			writer.writerow(write_dict)
file1.close()
print "done"



