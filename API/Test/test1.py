import requests
import time

def get_users():
    api_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return 'ERROR'

def get_todos():
    api_url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()[:10:]
    return 'ERROR'

def get_titles():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()[:10:]
    return 'ERROR'

def an():
    while True:
        print('INPUT NUMBER 1 OR 2 OR 3')
        number = int(input('NUMBER = '))
        if number == 1:
            for user in get_users():
                print(f"ID : {user['id']} -> {user['username']} -> {user['email']}")
                time.sleep(0.5)
            ctn = input('continue (y/n) : ')
            if ctn == 'n' : break
            print('---------------------------')
        elif number == 2:
            for todo in get_todos():
                print(f"ID : {todo['id']} -> {todo['title']}")
                time.sleep(0.5)
            ctn = input('continue (y/n) : ')
            if ctn == 'n' : break
            print('---------------------------')
        elif number == 3:
            for todo in get_todos():
                print(f"ID : {todo['id']} -> {todo['title']}")
                time.sleep(0.5)
            ctn = input('continue (y/n) : ')
            if ctn == 'n' : break
            print('---------------------------')
        else:
            print('ERROR, Please Enter Again !!!!')
            ctn = input('continue (y/n) : ')
            if ctn == 'n' : break
            print('---------------------------')

an()