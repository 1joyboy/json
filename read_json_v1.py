import json as js

with open('input.json', 'r') as red:
    data = js.load(red)

# print(type(data))
new_list =[]
for i in data:
    # print(i)
    # print(type(i))
    # print(i['name'])
    # role_name=i['name']
    for key,value in i.items():
        if key == 'name':
            new_dict = {}
            new_dict[key] = value
            new_dict['description'] = ""
    # print(new_dict)
    # break
    new_list.append(new_dict)
print(new_list)

with open('output.json', 'w') as new_file:
    # new.write(new_list.replace('    ', '  '))
    js.dump(new_list, new_file, indent=2)









# DRAFT
#         print('"'+key+'":','"'+value+'",'+"\n"+'"description": ""')
#         json_string = '"' + key + '":','"' + value + '",'+ "\n" + '"description": ""'
#         print(json_string)
#         json_object = js.loads(json_string)
#         print(json_object)
# DRAFT