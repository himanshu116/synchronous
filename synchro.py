from threading import *
import time
l=Lock()
def display(name):
	l.aquire()
	for i in range(10):
		print("gudmrnh:",end="--->")
		time.sleep(1)
		l.release()
t1=Thread(target=display,args=("pratipal"))
t2=Thread(target=display,args=("tanush"))
t3=Thread(target=display,args=("chiki"))
t1.start()
t2.start()
t3.start()