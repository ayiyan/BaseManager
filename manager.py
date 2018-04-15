#!/usr/bin/python
# -*- coding: UTF-8 -*-
#This is Manager
import random
import subprocess
import time
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import  Process,Queue

class QueueManager(BaseManager):
    pass

push_send_queue = Queue()
pull_receive_queue =  Queue()

QueueManager.register('get_task_queue', callable=lambda:push_send_queue)
QueueManager.register('get_result_queue', callable=lambda:pull_receive_queue)

master = QueueManager(address=('0.0.0.0', 50000), authkey=b'jerry')

master.start()

pull = master.get_result_queue()
push = master.get_task_queue()

print("i am master...")

send_message = "memory"
push.put(send_message)

receive_message = pull.get()
print("receive message : %s " % (receive_message))

master.shutdown()