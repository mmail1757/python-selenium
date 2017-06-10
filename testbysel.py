import unittest
from po.abstractpo import MainPage, SearchResultsPage
from scripts.wrapper import Wrapper

__author__ = 'user'


class TestBySelenium(unittest.TestCase):

    expected_price = 1960
    commodity = "D-Link DIR-826L"

    def setUp(self):
        #self.driver = Wrapper().getDriver()
        self.driver1 = Wrapper().getDriver()
        #print(self.driver is self.driver1)
        self.driver1.get("http://rozetka.com.ua")

    def test_search_certain_commodity(self):

        mainPage = MainPage(self.driver)
        mainPage.search_some_commodity(self.commodity)
        resultsPage = SearchResultsPage(self.driver)
        assert resultsPage.is_commodity_enable() == True, "This commodity " + self.commodity + " doesn't available at this time"
        price = resultsPage.get_commodity_price()
        assert price == self.expected_price, "Commodity price is wrong, expected price" + str(self.expected_price)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()