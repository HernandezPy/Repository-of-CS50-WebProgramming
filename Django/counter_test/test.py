import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTest(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri('counter.html'))
        self.assertEqual(driver.title, 'Counter Test')

    def test_button_click(self):
        driver.get(file_uri('counter.html'))
        button = driver.find_element("id", "increase")
        button.click()
        counter = driver.find_element("id", "value")
        self.assertEqual(counter.text, '1')

    def test_multiple_clicks(self):
        driver.get(file_uri('counter.html'))
        button = driver.find_element(by="id", value="increase")
        for _ in range(5):
            button.click()
        counter = driver.find_element(by="id", value="value")
        self.assertEqual(counter.text, '5')

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

if __name__ == "__main__":
    unittest.main()