#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import subprocess
import time
import socket
import  queue
from multiprocessing.managers import BaseManager
from multiprocessing import  Process, Queue

class QueueManager(BaseManager):
    pass

while True:
    print("start!!!")
    while True:
        try:
            sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sc.settimeout(2)
            sc.connect(("192.168.1.105",50000))
            sc.close()
        except:
            print("Server already halt!!!")
            time.sleep(3)
        else:
            print("*****Server already start!!!*****")
            time.sleep(3)
            break
    try:
        QueueManager.register('get_task_queue', callable=lambda:push_send_queue)
        QueueManager.register('get_result_queue', callable=lambda:pull_receive_queue)
        master = QueueManager(address=("192.168.1.105", 50000), authkey=b'jerry')
        master.connect()
        push = master.get_result_queue()
        pull = master.get_task_queue()

        print("i am client, get message ...")

        reveive_message = pull.get()
        print(reveive_message)
        send_message=500
        push.put(send_message)
        time.sleep(5)
    except:
        print("Error")
    # master.shutdown()



