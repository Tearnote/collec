import multiprocessing

bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '/var/log/gunicorn/collec-access.log'
errorlog = '/var/log/gunicorn/collec-error.log'
pidfile = '/var/run/gunicorn/collec.pid'
