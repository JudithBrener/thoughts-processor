import datetime
import socket

from cli import CommandLineInterface
from connection import Connection
from thought import Thought

cli = CommandLineInterface()


def upload_thought(address, thought):
    data = thought.serialize()
    sock = socket.socket()
    sock.connect(address)
    connection = Connection(sock)
    connection.send(data)
    connection.close()


@cli.command
def upload(address, user, thought):
    address_lst = address.split(":")
    address_as_tuple = (address_lst[0], int(address_lst[1]))
    t = Thought(int(user), datetime.datetime.now(), thought)
    upload_thought(address_as_tuple, t)
    print('done')


if __name__ == '__main__':
    cli.main()
