
from selenium import webdriver

#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from Tests.utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
from pageobjects.Homepage import Homepage
from pageobjects.checkoutpage import Checkoutpage


class TestOne(BaseClass):

    def test_e2e(self):
        homePage= Homepage(self.driver)
        CheckOutpage = homePage.shopitems()
        products = CheckOutpage.getcardtitles()
        for product in products:
            prodcutName = product.find_element_by_xpath("div/h4/a").text
            if prodcutName == "Blackberry":
                product.find_element_by_xpath("div[2]/button").click()


