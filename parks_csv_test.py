import csv
import pprint

# a_list = []
# f = open('filename.csv', 'r')
# reader = csv.reader(f)
# for row in reader:
#     a_list.append(row)
#
# f.close()

# with open('park.csv', 'r') as file:
#     reader = csv.reader(file)
#     park_list = list(reader)
#
# pprint.pprint(park_list)

with open('park.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        # print(row['park.key'], row['park.name'], row['park.alias'],
        #       row['city'], row['state'], row['country'])