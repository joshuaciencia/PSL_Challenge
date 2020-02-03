#!/usr/bin/python3
"""
test module for the platform
"""
import requests as r
import unittest

class TestStringNumbers(unittest.TestCase):
    """ test imput string numbers """
    url = 'http://127.0.0.1:5000'

    def test_word1(self):
        """ test simple word """
        data = {'Amazonas': 'six'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('6', num)

    def test_word2(self):
        """ test simple word """
        data = {'Antioquia': 'tenthousandthreehundredfour'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('10304', num)

    def test_word3(self):
        """ test simple word """
        data = {'Atlantico': 'perrito'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('0', num)
    def test_word4(self):
        """ test simple word """
        data = {'Nariño': 'sixti'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('0', num)
    def test_number(self):
        """ test string number"""
        data = {'Meta': '13453'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('13453', num)

    def test_negative(self):
        """ test negative number """
        data = {'Sucre': '-103'}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('0', num)

    def test_empty(self):
        """ test empty field """
        data = {'Choco': ''}
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('0', num)

    def test_multiple_states(self):
        """ test multiple states """
        data = {
                'Amazonas': 'forty',
                'Huila': 'tenthousand',
                'Tolima': '10',
                'Antioquia': 'quince',
                'Cordoba': '-83'
                }
        num = r.post(self.url, data=data).content.decode('utf-8')
        num = num.split(':')[-1].strip()
        self.assertEqual('10050', num)

if __name__ == '__main__':
    unittest.main()
