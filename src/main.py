from _init_ import start
import threading as th


th.Thread(target=start,args=("d1",13.0822,80.2755,)).start()
th.Thread(target=start,args=("d2",12.9941,80.1709,)).start()
th.Thread(target=start,args=("d3",13.06745,80.20566,)).start()
