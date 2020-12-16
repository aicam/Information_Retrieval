from progressbar import *
import time

widgets = ['Test: ', Percentage(), ' ', Bar(marker='0',left='[',right=']'),
           ' ', ETA(), ' ', FileTransferSpeed()] #see docs for other options

pbar = ProgressBar(widgets=widgets, maxval=500)
pbar.start()
pbar.update(5)
time.sleep(1)
pbar.update(5)
# for i in range(100):
#     time.sleep(1)# here do something long at each iteration
#     pbar.update(i*5) #this adds a little symbol at each iteration
time.sleep(2)
pbar.finish()