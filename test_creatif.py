#coding:utf-8
import os 
import unittest
from fonction import detection

class TestCrypto(unittest.TestCase):
    def testFonction(self):
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
if __name__ == '__main__':
    unittest.main()
os.system("pause")