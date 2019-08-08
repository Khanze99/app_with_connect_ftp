import pysftp
import getpass
import threading

CHECK = False
CONFIG = {}
USER_CONFIG = {}
COMMANDS = {'/help': '1. </connect> - connect to ftp example \n2. </copy FROM TO>\n4. /info about server\n3. /exit ',
            '/connect': '',
            '/copy': '',
            '/exit': "Thank's good bye :)",
            '/info': ''}
TURN_LIST = []

# host = "127.0.0.1"
# user = "-"
# password = "-"


def copy_local_to_server(from_path, to_path):
    with pysftp.Connection(**USER_CONFIG) as ftp:
        print("Find file to local directory")
        try:
            ftp.put(from_path, to_path)
        except FileNotFoundError:
            print("Dont such file")
        print("Save file to server...")


def get_info_about_server(**data):
    with pysftp.Connection(**data) as ftp:
        print("Connected to {}...".format(data['host']))
        hostname = ftp.execute('hostname')[0].decode("ascii").strip()
        CONFIG.update({'hostname': hostname})
        for item in CONFIG:
            print("{} - {}".format(item, CONFIG[item]))


def connected_to_ftp(**data):
    with pysftp.Connection(**data) as ftp:
        print("Connected to {}...".format(data['host']))


if __name__ == "__main__":
    while True:
        if CHECK is False:
            print("-----------------------------HELLO-------------------------------\n"
                  "...........input /help for the check commands....................\n"
                  "...........--------------------------------------------..........\n"
                  "...........input /connect for get info about ftp-server..........\n"
                  "...........--------------------------------------------..........\n"
                  "...........input /copy TO FROM - copied file to ftp-server..........")
            CHECK = True
        command = input('Write command :')
        if command == '/help':
            print(COMMANDS['/help'])
            input("Press any button to continue")
            continue
        if command == "/connect":
            USER_CONFIG.update({'host': input("Please enter your host: "),
                                'username': input("Please enter your username: "),
                                'password': getpass.getpass("Input your password: ")})
            CONFIG.update({'host': USER_CONFIG['host'], 'username': USER_CONFIG['username']})
            connected_to_ftp(**USER_CONFIG)
            continue
        if command == '/info':
            if len(CONFIG) == 0:
                print("---------------------------------------------------------\n"
                      "You need connect to the ftp-server. Give command /connect\n"
                      "----------------------------------------------------------")
                continue
            get_info_about_server(**USER_CONFIG)
            continue
        if command == '/copy':
            from_path = input('Please input path to file in pc: ')
            to_path = input('Please input path to ftp-server: ')
            CONFIG.update({'from': from_path, 'to': to_path})
            copy_local_to_server(from_path, to_path)
            continue
        if command == '/exit':
            print(COMMANDS['/exit'])
            break
        else:
            print("I can not find this {}".format(command))

