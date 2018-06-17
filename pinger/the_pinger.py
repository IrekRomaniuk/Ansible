#!/usr/bin/env python
# ping a list of host with threads for increase speed
# use standard linux /bin/ping utility
# forked from sourceperl/th_pinger.py
# https://gist.github.com/irom77/794c18ba392e42e944b09c42493b1786

from threading import Thread
import subprocess
import Queue
import re
import os
import sys

# some global vars
num_threads = 100
ips_q = Queue.Queue()
out_q = Queue.Queue()


# build IP array
ips = []
payload={}
payload['msg']=[]

dir = os.path.dirname(os.path.abspath(__file__))
targets_file = os.path.join(dir, "pinglist.txt")
# print targets_file
try:
  with open(targets_file, 'r') as f:
    ips = f.readlines()
except IOError:    
  for i in range(1,200):
    ips.append("10.192."+str(i)+".1")
    
# print("First: {} Last: {}".format(ips[0],ips[len(ips)-1]))
print('Numbers of address to ping {}'.format(len(ips)))
# sys.exit(0)
# thread code : wraps system ping command
def thread_pinger(i, q):
  """Pings hosts in queue"""
  while True:
    # get an IP item form queue
    ip = q.get()
    # ping it
    args=['/bin/ping', '-c', '1', '-W', '1', str(ip)]
    p_ping = subprocess.Popen(args,
                              shell=False,
                              stdout=subprocess.PIPE)
    # save ping stdout
    p_ping_out = p_ping.communicate()[0]

    if (p_ping.wait() == 0):
      # rtt min/avg/max/mdev = 22.293/22.293/22.293/0.000 ms
      search = re.search(r'rtt min/avg/max/mdev = (.*)/(.*)/(.*)/(.*) ms',
                         p_ping_out, re.M|re.I)
      ping_rtt = search.group(2)
      out_q.put("OK " + str(ip) + " rtt= "+ ping_rtt)

    # update queue : this ip is processed
    q.task_done()

# start the thread pool
for i in range(num_threads):
  worker = Thread(target=thread_pinger, args=(i, ips_q))
  worker.setDaemon(True)
  worker.start()

# fill queue
for ip in ips:
  ips_q.put(ip.replace("\n",""))

# wait until worker threads are done to exit
ips_q.join()

# print result
while True:
  try:
    msg = out_q.get_nowait()
  except Queue.Empty:
    break
  # print msg
  payload['msg'].append(msg)
print len(payload['msg'])  