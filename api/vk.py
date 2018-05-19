import matplotlib.pyplot as plt
import vk_api
import json

session = vk_api.VkApi(login='LOGIN',token='TOKEN')
session.auth()
vk = session.get_api()

friends=vk.friends.get()
ids = friends['items']

tmp = [id for id in ids]

def dump(file_name,data):
    f = open(file_name,"w+")
    json.dump(data, f)


def friends_of_frinds_count():
    x = []
    y = []
    z = {}
    for id in tmp:
        user = vk.users.get(user_ids=id)[0]
        if 'deactivated' not in user:
            user_name = user['first_name'] + ' ' + user['last_name']
            user_friends_count = vk.friends.get(user_id=id,fields='name,lists')['count']
            x.append(user_name)
            y.append(user_friends_count)
            z[user_name] = user_friends_count
    dump('user_friends_count.json', z)
    x_axe = [c for c in range(0, len(x))]
    plt.xticks(x_axe, x, rotation=45, fontsize=7)
    plt.scatter(x_axe,y)
    plt.show()


def create_friends_dump():
    my_friends = {}
    for id in tmp:
        user = vk.users.get(user_ids=id)[0]
        if 'deactivated' not in user:
            user_name = user['first_name'] + ' ' + user['last_name']
            user_friends_count = vk.friends.get(user_id=id,fields='lists')['count']
            user_friends = vk.friends.get(user_id=id,fields='lists')['items']
            details = {}
            their_friends = {}
            for user_friend in user_friends:
                their_friends[str(user_friend['id'])] = user_friend['first_name'] + ' ' + user_friend['last_name']
                details['name'] = user_name
                details['count'] = user_friends_count
                details['friends'] = their_friends
            my_friends[str(id)] = details
    dump('user_friends.json', my_friends)


def get_friends_of_friend():
    json_file = open('user_friends.json')
    data = json.load(json_file)
    friends_and_their_friend = {}
    for friend_id in data:
        friend_name = data[friend_id]['name']
        their_friends = data[friend_id]['friends']
        their_friends_ids = [x for x in their_friends]
        friends_and_their_friend[friend_name] = their_friends_ids
    return friends_and_their_friend


def get_mutual_friends():
    friends_of_friends = get_friends_of_friend()
    counts = {}
    for friend in friends_of_friends:
        their_friends_ids = friends_of_friends[friend]
        for id in their_friends_ids:
            if id in counts:
                counts[id] += 1
            else:
                counts[id] = 1
    return counts


def get_leaders(count):
    counts = get_mutual_friends()
    leaders = {}
    x = []
    y = []
    for id in counts:
        if counts[id] > count:
            user = vk.users.get(user_ids=id)[0]
            user_name = user['first_name'] + ' ' + user['last_name']
            leaders[user_name] = counts[id]
            x.append(user_name)
            y.append(counts[id])
    dump('leaders.json', leaders)
    x_axe = [c for c in range(0, len(x))]
    plt.xticks(x_axe, x, rotation=45, fontsize=7)
    plt.scatter(x_axe,y)
    plt.show()


friends_of_frinds_count()
create_friends_dump()
get_leaders(5)