import unittest
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import _init_


class RequestDemo_hyperlinks_buttons_images(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome( _init_.path3 )
        self.file1 = open( _init_.path2 + "Testcaseresults_request_demo.csv", "a+" )

    def test_Request_Demo_video_play(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/test-request-xeneta-demo")
        driver.maximize_window()
        driver.implicitly_wait(5)
        try:

            driver.find_element_by_xpath("//div[@id = 'hs_cos_wrapper_widget_1505999963669']").click()
            self.file1.writelines("TestCase1.2.1" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')
            driver.implicitly_wait( 20 )
        except:
            self.file1.writelines("TestCase1.2.1"+" "+"Failed" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')

        driver.get_screenshot_as_file( _init_.path1 + "TestCase1.2.1" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Request_Demo_Book_Demo(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/test-request-xeneta-demo")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_link_text('BOOK DEMO').click()
        driver.implicitly_wait(20)
        self.file1.writelines("TestCase1.2.2" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')
        driver.get_screenshot_as_file( _init_.path1 + "TestCase1.2.2" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Request_Demo_News_Letter_signup(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/test-request-xeneta-demo")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//div[@id = 'hs_form_target_module_1490890020720863_Footer_form']/form/div[1]/div/input").send_keys("test1234566@testttt.com")
        driver.find_element_by_name('confirm_opt_in').click()
        driver.find_element_by_xpath("//input[@data-reactid = '.hbspt-forms-1.4.1.0']").click()
        driver.implicitly_wait(15)
        successmsg = driver.find_element_by_id('hs_form_target_module_1490890020720863_Footer_form').get_attribute("innerHTML")
        if successmsg == "Success! Thank you for signing up to the Xeneta newsletter!":
            self.file1.writelines("TestCase1.2.3" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')
        else:
            self.file1.writelines("TestCase1.2.3" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
        driver.get_screenshot_as_file( _init_.path1 + "TestCase1.2.3" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Request_Demo_customers(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/test-request-xeneta-demo")
        driver.maximize_window()
        driver.implicitly_wait(5)
        url = driver.find_element_by_xpath("//div[@class = 'logo-list horizontal-overflow']/a").get_attribute("href")
        if url == "https://www.xeneta.com/customers":

            self.file1.writelines("TestCase1.2.4" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
        else:
            self.file1.writelines("TestCase1.2.4" + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        driver.implicitly_wait(15)
        driver.find_element_by_xpath( "//h2[@class = 'small-caps-heading heading']" ).click()
        self.file1.writelines( "TestCase1.2.5" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
        driver.get_screenshot_as_file( _init_.path1 + "TestCase1.2.4" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def tearDown(self):
        self.file1.close()

if __name__ == "__main__":
    unittest.main()
