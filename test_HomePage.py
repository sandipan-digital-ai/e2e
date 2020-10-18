from selenium.webdriver.chrome import webdriver


class TestHomePage:

    def test_formsubmission(self):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.rahulshettyacademy.com/angularpractice")

        driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        driver.find_element_by_id("country").send_keys("ind")
        #verifylinkpresence("India")
        driver.find_element_by_link_text("India").click()
        driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        driver.find_element_by_css_selector("[type='submit']").click()
        successText = (self.driver.find_element_by_class_name("alert-success").text)
        assert "Success! Thank you!" in successText