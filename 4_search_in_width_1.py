from collections import deque

my_friends = {'my': ['Mikhael', 'Alice', 'Georg'],
              'Mikhael': ['Tom', 'Gym'],
              'Alice': ['Lyk', 'Teddy', 'Alice'],
              'Georg': ['Sam', 'Grace', 'Rikki', 'Mikhael'],
              'Tom': ['Teddy'],
              'Gym': [],
              'Lyk': ['Teddy'],
              'Teddy': [],
              'Sam': [],
              'Grace': ['Teddy'],
              'Rikki': []
              }


def seller(name):
    if 'y' in name.lower():
        return True
    else:
        return False


def search_seller(name):
    search = deque()
    search += my_friends[name]
    searched = []
    while search:
        person = search.popleft()
        if person not in searched:
            if seller(person):
                print(f'Men {person} is seller!!!')
                return True
            else:
                search += my_friends[person]
                searched.append(person)
    print('You dont have friends who is seller')


search_seller('my')
