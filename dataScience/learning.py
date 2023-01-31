users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7),
    (6, 8), (7, 8), (8, 9)
]

print(users[0]['name'])
print(users[9]['id'])

# create am empty friends list to the users
for user in users:
    user['friends'] = []

# insert friends names according to the friendship list tuples
for i, j in friendships:  # unpacking the tuple in friendship list
    users[i]['friends'].append(users[j]['name'])
    users[j]['friends'].append(users[i]['name'])


# for user in users:
#     print(user)


# finding the number of friends each user have

def number_of_friends(user):
    """
    Return the number of friends a user have depending on the length of the
    friends list
    :param user: user at certain index
    :return: int
    """
    return len(user['friends'])


# total number of connection on the users list
total_connection = sum(number_of_friends(user) for user in users)
# print(total_connection)

print('*' * 60)
# accessing users friends
# print(number_of_friends(users[0]))

# average connection
num_of_users = len(users)
avg_connections = total_connection // num_of_users  # int division

# finding the users with most connections, sort the list according to friend
# list
num_of_friends = [(user['id'], number_of_friends(user)) for user in users]
print(num_of_friends)

# sorting the Users according to the number of friends using lambdas
# num_of_friends.sort(key=lambda x: x[1], reverse=True)
num_of_friends = sorted(num_of_friends, key=lambda x: x[1], reverse=True)

print(num_of_friends)
