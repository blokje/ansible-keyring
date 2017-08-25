#!/usr/bin/env python3

import argparse
import getpass
import keyring

try:
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
except ImportError:
    pass

def main():
    parser = argparse.ArgumentParser('ansible-keyring')
    subparsers = parser.add_subparsers(help='command', title="commands", dest="command")
    parser_set = subparsers.add_parser('set', help="Add password to the keyring")
    parser_get = subparsers.add_parser('get', help="Remove password from the keyring")

    parser_set.add_argument('name')
    parser_set.add_argument('password', nargs='?')
    parser_get.add_argument('name')

    args = parser.parse_args()
    if not args.command:
        parser.error("Missing action")

    if args.command == "set": set_password(args.name, args.password)
    if args.command == "get": get_password(args.name)

def set_password(name, password=None):
    if not password:
        password = getpass.getpass("Password: ")
        if password == getpass.getpass("Repeat password: "):
            keyring.set_password('ansible-keyring', name, password)
            print("Password set")
            return
    print("Password not set")

def get_password(name):
    try:
        password = keyring.get_password("ansible-keyring", name)
        if password:
            print(password)
    except:
        pass

if __name__ == '__main__':
    main()
