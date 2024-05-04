import requests


user_input = input("enter id:")
get_url = "https://jsonplaceholder.tyicode.com/todos/15"

get_response = requests.get(get_url)
print(get_response.json())

to_do_item_15 = {"userId": 2, "title": "put title","completed": False}
#put_response = requests.put(get_url,json= to_do_item_15)
#print(put_response.json())

to_do_item_patch_15 = {"title": "Patch Test"}
#patch_response = requests.patch(get_url,json=to_do_item_patch_15)
#print(patch_response.json())

#Delete
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)