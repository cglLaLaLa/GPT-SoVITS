import threading

class SingletonConcurrentHashMap(object):
    instance = None
    lock = None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = {}
            cls.lock = threading.Lock()
            return cls
        else:
            return cls

    def add(self, key, value):
        self.lock.acquire()
        self.instance[key] = value
        self.lock.release()

    def remove(self, key):
        self.lock.acquire()
        self.instance.pop(key)
        self.lock.release()

    def get(self, key):
        self.instance.get(key)