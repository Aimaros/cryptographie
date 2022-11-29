#coding:utf-8
import os 
import unittest
from fonction import detection

class TestCrypto(unittest.TestCase):
    def testFonction(self):
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
        self.assertEqual(detection("ALLER AU TOILETTE", "ELEMENT"),"EWPQV NN XZMXIGMI")
        self.assertEqual(detection("JE SUIS UN DEVELOPPEUR", "PRO"),"YV GJZG JE RTMSAFDEVIG")
        self.assertEqual(detection("NOUS SOMMES DES GAGNANTS", "HEUREUX"),"USOJ WIJTIM UIM DHKHRRNP")
        self.assertEqual(detection("BONJOUR", "JE MANGE"),"KS-VOHX")
        self.assertEqual(detection("ENEAM", "AZERTY"),"EMIRF")
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
        self.assertEqual(detection("BONJOUR", "FEU"),"GSHOSOW")
        
if __name__ == '__main__':
    unittest.main()
os.system("pause")