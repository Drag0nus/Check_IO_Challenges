import re

data = []
f = open("pii-exportTID1.csv")
regexp = r'^"*(\d+)\|(.+?)\|(.+?)\|(\d+?)\|(\d+?)"*,*$'
value_regexp = r'"+(.+?)"+'

rows = []
print('read and parse file')
i = 0
for row in f:
    if i != 0 and i % 1000 == 0:
        print("progress: " + str(i))
    i += 1
    match = re.match(regexp, row)
    if match:
        values = re.findall(value_regexp, match.group(3)[3:-3])
        res = {}
        if values:
            res['id'] = match.group(1)
            res['name'] = match.group(2)
            res['value'] = values
            res['candidate_id'] = match.group(4)
            rows.append(res)
        else:
            print("invalid row: " + row)
    elif row:
        print("invalid row: " + row)
print("progress: " + str(i) + ", end")
print()


print('group candidates')
candidates = {}
names = set()
i = 0

for row in rows:
    if i != 0 and i % 1000 == 0:
        print("progress: " + str(i))
    i += 1
    names.add(row['name'])
    candidates_array = candidates.get(row['candidate_id'])
    if candidates_array:
        candidates_array.append(row)
    else:
        candidates[row['candidate_id']] = [row]
print("progress: " + str(i) + ", end")
print()


print('write results')
i = 0
names = [x for x in names]
result_f = open("result.csv", "x")
result_f.write('ID|' + '|'.join(names) + '\n')
for (id, candidate) in candidates.items():
    if i != 0 and i % 1000 == 0:
        print("progress: " + str(i))
    i += 1

    result = []
    for name in names:
        value = ''
        for row in candidate:
            if row['name'] == name:
                value = ', '.join(row['value'])
        result.append(value)
    result_f.write(str(i) + '|' + '|'.join(result) + '\n')
result_f.close()
print("progress: " + str(i) + ", end")
