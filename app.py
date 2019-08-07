import pysftp
import getpass

CONFIG = {}

# host = input("Please enter your host: ")
host = "127.0.0.1"
# user = input("Please enter your username: ")
user = "-"
# password = getpass.getpass("Input your password")
password = "-"

with pysftp.Connection(host=host, username=user, password=password) as ftp:
    print("Connected ...")
    ftp.put('test.txt', "/home/khanze/files/test.txt")
