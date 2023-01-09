import unittest
import os
from FileHelper import *
import UnzipHelper

class MyTestCase(unittest.TestCase):
    def test_something(self):
        Note = open(os.path.join(r"D:\Projects\CJM\M-SRM", 'err.txt'),mode='w')
        err=["1","2","2"]
        for e in err:
            Note.write(str(e))
        Note.flush()
        Note.close()

        # for i in range(0,99):
        #     print("{:0>3d}".format(i))


if __name__ == '__main__':
    unittest.main()
