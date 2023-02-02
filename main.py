import requests
import json


response=requests.get('https://jsonplaceholder.typicode.com/todos')
todos=json.loads(response.text)
# print(todos[:10])
# print(type(todos))
todos_by_user={}
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo["userId"]]+=1
        except KeyError:
            todos_by_user[todo["userId"]]=1
print (todos_by_user)
top_users=sorted(todos_by_user.items(),key=lambda x:x[1],reverse=True)
print(top_users)
max_complete=top_users[0][1]
print (max_complete)
users=[]
for user, num_complete in top_users:
    if num_complete<max_complete:
        break
    users.append(str(user))
print(users)
max_users=" and ".join(users)
s="s" if len(users)>1 else ""
print (f"User{s } {max_users} copleted {max_complete} TOdos")