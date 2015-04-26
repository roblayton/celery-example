from __future__ import absolute_import
from celery import Celery

# initialize with defaults
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def fiblist(n):
  return list(fib(n))

def fib(n):
  a,b = 1,1
  for i in xrange(n-1):
    a,b = b, a+b
    yield a
