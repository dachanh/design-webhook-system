import os
import multiprocessing


# Logging
accesslog = "/logs/access.log" 
errorlog = "/logs/error.log"  
os.makedirs('/logs',exist_ok=True)
loglevel = "debug"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'