#! /usr/bin/env python
# gives http://www.pythonchallenge.com/pc/return/italy.html

from xmlrpc.client import ServerProxy, Error

if __name__ == '__main__':
    server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    try:
        # resp = server.system.listMethods()
        resp = server.phone('Bert')
        print(resp)
    except Error as err:
        print(err)
