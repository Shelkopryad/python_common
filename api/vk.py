import matplotlib.pyplot as plt
import vk_api
import json

session = vk_api.VkApi(login='LOGIN',token='TOKEN')
session.auth()
vk = session.get_api()

friends=vk.friends.get()
ids = friends['items']

tmp = [id for id in ids]
x = []
y = []
z = {} # создадим дамп

for id in tmp:
    user = vk.users.get(user_ids=id)[0]
    if 'deactivated' not in user:
        user_name = user['first_name'] + ' ' + user['last_name']
        user_friends_count = vk.friends.get(user_id=id,fields='name,lists')['count']
        x.append(user_name)
        y.append(user_friends_count)
        z[user_name] = user_friends_count

f = open("result.json","w+")
json.dump(z, f)

x_axe = [c for c in range(0, len(x))]
plt.xticks(x_axe, x, rotation=45, fontsize=7)
plt.scatter(x_axe,y)
plt.show()