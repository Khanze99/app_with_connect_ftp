from loguru import logger
import pysftp
import threading
import json
import time

CHECK = False
TURN_LIST = []
logger.add('ftp_connect.log')
# host = "127.0.0.1"
# user = "-"
# password = "-"


def parse_config():
    while True:
        if len(TURN_LIST) == 0:
            time.sleep(5)
        for item in TURN_LIST:
            try:
                with open(command, mode='r') as config:
                    logger.debug("Read config")
                    data = json.load(config)
            except FileNotFoundError:
                logger.debug("I can not find the config")
            copy_local_to_server(**data)
            TURN_LIST.remove(item)


def copy_local_to_server(**data):
    host = data['host']
    from_path = data['from_path']
    to_path = data['to_path']
    try:
        valid_open = open(from_path, mode="r")
        valid_open.close()
    except FileNotFoundError:
        logger.debug("Can not find the file")
        return False
    try:
        with pysftp.Connection(host=host, username=data['username'], password=data['password']) as ftp:
            logger.debug('Connect to {}'.format(host))
            ftp.put(from_path, to_path)
    except FileNotFoundError:
        logger.debug("Can not find path to save on the server")
        with pysftp.Connection(host=host, username=data['username'], password=data['password']) as ftp:
            logger.debug('Connect to {}'.format(host))
            file = from_path.split('/')[-1]
            ftp_dir = "ftp_files"
            pwd = ftp.pwd + '/'
            to_save = pwd+ftp_dir+'/'+file
            list_dirs = ftp.listdir()
            if ftp_dir not in list_dirs:
                ftp.mkdir(ftp_dir)
            ftp.put(from_path, to_save)
        logger.debug('Save to {}'.format(to_save))


if __name__ == "__main__":
    thread = threading.Thread(target=parse_config, name='thread 2')
    thread.start()
    while True:  # Thread 1
        if CHECK is False:
            print("-----------------------------HELLO-------------------------------\n"
                  ".................Enter the path to the config....................\n"
                  "...........--------------------------------------------..........\n"
                  ".......................input /exit to exit ......................\n"
                  "...........--------------------------------------------..........")
            CHECK = True
        command = input('Enter the path to the config or input /exit: ')
        if command == '/exit':
            logger.debug("Good bye :)")
            thread.join()
            break
        else:
            TURN_LIST.append(command)




