import unittest

__author__ = 'user'
from scripts.wrapper import Wrapper

class Test1(unittest.TestCase):


    def setUp(self):
        pass

    def test1(self):
        ar = set([1,1,1,1,0 ,3,5, 7])
        arr2 = set([2, 5, 9, 9, 11])
        # ar = [1, 0, 0, 0, 1, 1, 1]
        # ar = filter(lambda x: x == 1, ar)
        #
        # print ar
        # ar= "aaaabbbcccd"
        # ar = filter(lambda x: x != x, ar)
        print list(set(arr2) - set(ar))
if __name__ == "__main__":
    unittest.main()