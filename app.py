import pysftp
import getpass
import threading

CONFIG = {}
COMMANDS = {'/help': '1. </connect> - connect to ftp example \n2. </copy TO FROM>\n3. /exit ',
            '/connect': '',
            '/copy': '',
            '/exit': ''}
TURN_LIST = []

# host = "127.0.0.1"
# user = "-"
# password = "-"


def connected_to_ftp(host, user, password):
    with pysftp.Connection(host=host, username=user, password=password) as ftp:
        print("Connected ...")
        ftp.put('test.txt', "/home/khanze/files/test.txt")


if __name__ == "__main__":
    while True:
        print("Give me a command. You need list commands? Input /help\n"
              "...........--------------------------------------------..........\n"
              "...........input /connect for get info about ftp-server..........\n"
              "...........--------------------------------------------..........\n"
              "...........input /copy TO FROM - copied file to ftp-server..........")
        command = input()
        if command == '/help':
            print(COMMANDS['/help'])
            input("Continue?")

            continue
        if command == "/connect":
            user_config = {'host': input("Please enter your host: "),
                           'user': input("Please enter your username: "),
                           'password': getpass.getpass("Input your password: ")}
            connected_to_ftp(user_config['host'], user_config['user'], user_config['password'])
        if command == '/exit':
            print("Thank's. Good bye :)")
            break

