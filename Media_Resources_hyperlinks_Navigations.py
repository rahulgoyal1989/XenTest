import unittest
import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import _init_

class MediaResources_hyperlinks_navigation(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome( _init_.path3 )
        self.file = open( _init_.path + "TestData_Elements_media_resources_hyperlinks.csv", "r" )
        self.file1 = open( _init_.path2 + "Testcaseresults_media_resources.csv", "a+" )

    def test_Media_resources_page_navigation(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/media-resources")
        driver.maximize_window()
        driver.implicitly_wait(5)
        filedata = csv.reader( self.file, delimiter=';' )
        for line in filedata:
            if line[2] == "nav":
                try:
                    driver.find_element_by_link_text(line[1]).click()
                    self.file1.writelines(line[0] + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

                except:
                    self.file1.writelines(line[0] + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                time.sleep(2)

            time.sleep(2)
            driver.get_screenshot_as_file( _init_.path1 + line[0] + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Media_resources_hyperlinks_spokesperson(self):

        filedata = csv.reader(self.file, delimiter=';')
        for line in filedata:
            if line[2] == "jump":
                driver = self.driver
                driver.set_page_load_timeout(10)
                driver.get("https://www.xeneta.com/media-resources")
                driver.maximize_window()
                driver.implicitly_wait(5)
                try:
                    driver.find_element_by_link_text(line[1]).click()
                    driver.implicitly_wait(5)
                    spocpersonname = line[3]
                    if spocpersonname == driver.find_element_by_tag_name("h1").text:
                        self.file1.writelines(line[0] + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                    else:
                        self.file1.writelines(line[0] + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                except:
                    self.file1.writelines(line[0] + " " + "Exception occured" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                time.sleep(2)

    def tearDown(self):
        self.file1.close()
        self.file.close()

if __name__ == "__main__":
    unittest.main()
