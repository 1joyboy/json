import json as js
import re

with open('input.json', 'r') as red:
    data = js.load(red)
# print(type(data))

for i in data:
    # print(i)
    # print(type(i))
    group = i['name']
    # print(group)
    account_id = i['accountId']
    # [print(account_id)]
    pattern = re.compile(r'^(aws)-([a-z0-9-]+)\.([a-z0-9-]+)\.([a-z0-9-]+)-([a-z0-9-]+)$')
    match = pattern.search(group)
    # print(match)
    if match:
        # print(match.group(0))
        # print(match.group(1))
        # print(match.group(2))
        # print(match.group(3))
        # print(match.group(4))
        # print(match.group(5))
        # print(match.group(6))
        new_group = f'aws#{match.group(3)}#{match.group(3)}_{match.group(4)}-{match.group(5)}#{account_id}'
        print(new_group)
    else:
        raise ValueError("Invalid group value")