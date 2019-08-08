import pysftp
import getpass
import threading

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


def get_info_about_server(**data):
    with pysftp.Connection(**data) as ftp:
        print("Connected to {}...".format(data['host']))
        hostname = ftp.execute('hostname')[0].decode("ascii")
        print(hostname)


def connected_to_ftp(**data):
    with pysftp.Connection(**data) as ftp:
        print("Connected to {}...".format(data['host']))


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
            input("Press any button to continue")
            continue
        if command == "/connect":
            USER_CONFIG.update({'host': input("Please enter your host: "),
                                'username': input("Please enter your username: "),
                                'password': getpass.getpass("Input your password: ")})
            CONFIG.update({'host': USER_CONFIG['host'], 'username': USER_CONFIG['username']})
            connected_to_ftp(**USER_CONFIG)
            while True:
                if input('Continue or exit?') == 'continue':
                    continue
                else:
                    print(COMMANDS['/exit'])
                    break
            break
        if command == '/info':
            get_info_about_server(**USER_CONFIG)
        if command == '/exit':
            print(COMMANDS['/exit'])
            break

