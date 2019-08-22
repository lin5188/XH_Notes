
# 书本1.4.1多进程
# 3.multiprocessing模块Pool类

'''
from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('Task %s (pid = %s) is running...' % (name,os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)

if __name__ ==  '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join() # 调用join()之前必须先调用close()
    print('All subprocesses done.')
'''

# 4.进程间通信
# Queue例子

'''

from multiprocessing import Process,Queue
import os,time,random

def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:

        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__ == '__main__':
    q = Queue()
    proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2 = Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
    proc_reader = Process(target=proc_read,args=(q,))

    proc_writer1.start()
    proc_writer2.start()

    proc_reader.start()

    proc_writer1.join()
    proc_writer2.join()

    proc_reader.terminate()
    
'''
