#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import multiprocessing

class monitor:

    def __init__(self):
        pass

    def write(self, ipaddr, q):
        print(ipaddr)
        val=subprocess.Popen("ssh root@%s '/bin/sh /script/mem.sh'" %(ipaddr),  stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        mem_info = val.stdout.read()
        mem_info = (str(mem_info, encoding='utf-8')).strip('\n')
        q.put(mem_info)

    # def read(self, q2 ):
    #     memory = q2.get()
    #     print("收到内存空间：%s MB" %memory)


def proxy_read(q2):
    memory = q2.get()
    print("收到内存空间：%s MB" %memory)


if __name__=='__main__':
    q = multiprocessing.Queue()
    proxy = monitor()
    ip_list = ['192.168.1.108','192.168.1.103','192.168.1.108','192.168.1.108']
    for ipaddr in ip_list:
        process_write = multiprocessing.Process(target=proxy.write, args=(ipaddr, q, ))
        process_read = multiprocessing.Process(target=proxy_read, args=(q,))
        process_write.start()
        process_read.start()
    #memory = q2.get()
    #print("收到的客户端的内存空间：%s MB" %memory)





