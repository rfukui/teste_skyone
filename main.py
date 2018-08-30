#!/usr/bin/env python
import sys
from time import time
from math import ceil
ttask = 0
umax = 0
args = {
    0: "input1.txt",
    1: "5",
    2: "10"
}
filename = "input1.txt"
users = {}


def add_user(_id):
    users[str(_id)] = ttask


def remove_users(_users):
    for user in _users:
        users.pop(user)


def open_file():
    f = open(filename).readlines()
    print(f)
    return f


def get_qtd_all_users():
    return len(users)


def get_qtd_servers(qtd_all_users):
    return ceil(qtd_all_users / umax)


def get_output():
    total_users = get_qtd_all_users()
    users_by_servers = []
    for x in range(get_qtd_servers(get_qtd_all_users())):
        if total_users <= umax:
            users_by_servers.append(str(total_users))
        else:
            users_by_servers.append(str(umax))
        total_users -= umax

    return ",".join(users_by_servers)


def adjust_users(qtd_user):
    total_users = 0
    user_zero_procs = []
    for user in users:
        users[user] -= 1
        if users[user] == 0:
            user_zero_procs.append(user)

    remove_users(user_zero_procs)
    for x in range(0, qtd_user):
        add_user(_id=time())
    
    print(get_output())


def main():
    try:
        file = open_file()
    except FileNotFoundError as e:
        raise Exception("file not found")

    for qtd_user in file:
        try:
            usr = int(qtd_user)
            adjust_users(usr)
        except ValueError as e:
            pass
        
    while get_qtd_all_users():
        adjust_users(0)

if __name__ == '__main__':

    for k, arg in enumerate(sys.argv[1:]):
        args[k] = arg
    filename = args[0]
    ttask = int(args[1])
    umax = int(args[2])
    main()
