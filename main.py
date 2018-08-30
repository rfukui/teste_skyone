#!/usr/bin/env python
import sys
from time import time
from math import ceil
ttask = 0
umax = 0
args = {
    0: "input1.txt",
    1: "5",
    2: "10",
    3: "output.txt",
}
filename = "input1.txt"
servers = []
output_filename = "output.txt"


def get_free_server():
    server_num = 1
    for i, server in enumerate(servers):
        if len(servers[i]["users"]) < umax:
            return servers[i]["id"]
    sid = str(time())
    servers.append({"id": sid, "users": []})
    return sid


def add_user(uid, sid):
    for server in servers:
        if server["id"] == sid:
            server["users"].append({"id": uid, "tasks": ttask})


def remove_servers():
    server_no_users = []
    for server in servers:
        if len(server["users"]) == 0:
            server_no_users.append(server)
    for server in server_no_users:
        servers.remove(server)


def remove_users():
    for i, server in enumerate(servers):
        user_zero_procs = []
        for k, user in enumerate(servers[i]["users"]):
            servers[i]["users"][k]["tasks"] -= 1
            if servers[i]["users"][k]["tasks"] == 0:
                user_zero_procs.append(servers[i]["users"][k])
        for user in user_zero_procs:
            servers[i]["users"].remove(user)


def read_file():
    f = open(filename).readlines()
    return f


def add_users(qtd_user):

    for x in range(0, qtd_user):
        add_user(str(time()), get_free_server())


def get_servers_snapshot():
    output = []
    for server in servers:
        output.append(str(len(server["users"])))
    if len(output):
        return ",".join(output) + "\n"
    return "0\n"


def get_qtd_servers():
    return len(servers)


def add_line(line, file):

    file.write(line)


def open_file():
    return open(output_filename, "w")


def main():
    try:
        file = read_file()
    except FileNotFoundError as e:
        raise Exception("file not found")

    output_file = open_file()

    for qtd_user in file:
        remove_users()
        remove_servers()
        try:
            usr = int(qtd_user)
            add_users(usr)
        except ValueError as e:
            pass
        add_line(get_servers_snapshot(), output_file)
    while get_qtd_servers():
        remove_users()
        remove_servers()
        add_line(get_servers_snapshot(), output_file)


if __name__ == '__main__':
    try:
        if sys.argv[1] in ("help", "?", "--help", "-help"):
            print("""
./main.py
executa o sistema para o arquivo imput1.txt com ttasks =5, umax = 10 e gera o arquivo
de saida output.txt
para mudar cada um dos items a sequencia é
./main.py <input file> <ttask> <umax> <outputfilename>
a ordem deve ser preservada
        """)
            sys.exit()
    except IndexError as e:
        pass
    

    for k, arg in enumerate(sys.argv[1:]):
        args[k] = arg
    filename = args[0]
    ttask = int(args[1])
    umax = int(args[2])
    output_filename = args[3]
    main()
