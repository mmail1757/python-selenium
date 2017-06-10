__author__ = 'user'
# -*- coding:utf-8 -*-
import unittest
import requests
from pyquery import PyQuery
import logging

class TestByRequest(unittest.TestCase):

    commodity = "D-Link+DIR-826L"
    availability = "Есть в наличии"
    expected_price = 1960


    def test_search_cirtain_commodity(self):

        r = requests.get('http://rozetka.com.ua/search/?section=/&text=D-Link+DIR-826L')
        assert self.commodity in r.text, "No page is next commodity found"
        pq = PyQuery(r.text)
        price_value = pq('div.g-i-list-price-uah')
        assert self.expected_price == int(filter(lambda x: x.isdigit(), price_value.text())), "Price doesn't match for commodity " + self.commodity + " expected price - " + str(self.expected_price)
        availability_value = pq('.g-i-list-status.available')
        a_value = availability_value.text().encode("utf-8")
        assert self.availability in a_value, "This commodity doesn't available"


if __name__ == "__main__":
    unittest.main()

