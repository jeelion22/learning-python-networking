import json

with open("books.json", "rt") as f:
    class_subj = json.load(f)

json_obj = json.dumps(class_subj)


employee = {"emp_name": "name", "emp_pos": "SD"}


print("python object")
print(class_subj)
print(type(class_subj))
# print("json object")
# print(json_obj)

# print(employee)

# print(type(employee))
# json_data = json.dumps(employee)

# print(json_data)

# print(type(json_data))
