import threading
import time
import logging

#IMPORTANT: 
#daemon threads are associated with tasks that can be interrupted with no consequences, the main program can quit with
#no regard to the state of its job. Exemple: monitoring heartbeat
#non- daemon threads are associated with tasks that must be completed before exiting. Exemple: filling database 

#task for the daemon thread
def daemon():
    logging.info('Starting my daemon job')
    time.sleep(2)
    logging.info('Done')

#task for the non-daemon thread
def non_daemon():
    logging.info('Starting my non-daemon job')
    logging.info('Done')

#creating the daemon thread 
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

#creating the non-daemon thread (default mode, no need to call setDaemon)
t = threading.Thread(name='non-daemon', target=non_daemon)

#starting threads
logging.info('Starting threads:')
d.start()
t.start()

#giving a 1 second chance to the daemon thread to finish its work, this is not mandatory of course
d.join(1)

#getting the status of the daemon thread at the end of the waiting time
if d.isAlive():
    daemonStatus = 'alive'
else:
    daemonStatus = 'terminated'

#waiting for the non-daemon thread to finish its work (indefinitely, because we really want it to finish the job before exiting)
t.join()
nonDaemonStatus = 'terminated'

#exiting
logging.info('Shutting down. Daemon thread:' + daemonStatus + ' Non-Daemon thread:' + nonDaemonStatus)
