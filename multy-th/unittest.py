import unittest
import threading
import socket
from mymulty import *
#from client1 import *

#Semaphores to lock the recv and accept methods
_recv_lock = threading.Condition()
_send_lock = threading.Condition()
_accept_lock = threading.Condition()


host = socket.gethostbyname(socket.gethostname())
port = 12345

class Test_setver(unittest.TestCase):

    def test_login(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))

        login_msg = "Login" + ":" + "clientName"
        conn.sendall(login_msg.encode())
        rec = conn.recv(1024).decode()
        conn.close()
        self.assertEqual(rec, "Login:clientName")

    def test_broadcast(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))

        msg = "msg" + ":" + "clientName" + ":" + "all" + ":" + "clientMessage"
        conn.sendall(msg.encode())
        rec = conn.recv(1024).decode()
        conn.close()
        self.assertEqual(rec, "clientName > clientMessage")

if __name__ == '__main__':
    unittest.main()



