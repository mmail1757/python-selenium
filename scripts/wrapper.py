from selenium import webdriver

__author__ = 'user'

class Wrapper(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def getDriver(self, *args, **kwargs):
        self.connection = webdriver.PhantomJS()
        return self.connection
