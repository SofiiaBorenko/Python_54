from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemoWebShopLocators:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demowebshop.tricentis.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_find_10_elements(self):
        d = self.driver
        elements = [
            # By.NAME
            d.find_element(By.NAME, "q"),
            d.find_element(By.NAME, "NewsletterEmail"),
            # By.CLASS_NAME
            d.find_element(By.CLASS_NAME, "ico-login"),
            d.find_element(By.CLASS_NAME, "ico-register"),
            d.find_element(By.CLASS_NAME, "search-box-button"),
            # By.ID
            d.find_element(By.ID, "small-searchterms"),
            d.find_element(By.ID, "newsletter-subscribe-button"),
            # By.CSS_SELECTOR
            d.find_element(By.CSS_SELECTOR, ".header-logo a"),
            d.find_element(By.CSS_SELECTOR, ".top-menu a[href='/books']"),
            d.find_element(By.CSS_SELECTOR, "input.search-box-text"),
        ]

        assert len(elements) == 10
        for el in elements:
            assert el.is_displayed()