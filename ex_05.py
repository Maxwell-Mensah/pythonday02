def my_add_elem_map(key, value, dict):
    dict[key]=value
    return dict

def my_modify_elem_map(key, value, dict):
    dict[key]=value
    return dict

def my_delete_elem_map(key, dict):
    del dict[key]
    return dict

def my_is_elem_valid(key, value, dict):
    for keys in dict:
        if keys==key and dict[keys]==value:
            return True
    return False

my_dict = {}
my_dict = my_add_elem_map("first", "baris", my_dict)
my_dict = my_add_elem_map("second", "toto", my_dict)
my_dict = my_add_elem_map("third", "life", my_dict)
my_dict = my_modify_elem_map("third", "42", my_dict)
my_dict = my_delete_elem_map("second", my_dict)
print(my_dict)

print(my_is_elem_valid("third", "42", my_dict))
