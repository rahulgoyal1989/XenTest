import unittest
import csv
import time
from datetime import datetime
from selenium import webdriver
import _init_


class MediaResources_language_Switcher(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome( _init_.path3 )
        self.file1 = open( _init_.path2 + "Testcaseresults_media_resources.csv", "a+" )

    def test_Media_resources_language_switcher_Deutsch(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/media-resources")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_link_text('Deutsch').click()
        try:
            if driver.find_element_by_tag_name('h1').text == "Pressematerialien":
               self.file1.writelines("SwitchToDeutsch" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
            else:
               self.file1.writelines("SwitchToDeutsch" + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        except:
            self.file1.writelines("SwitchToDeutsch" + " " + "Exception occurred" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
        time.sleep(5)
        driver.get_screenshot_as_file( _init_.path1 + "SwitchToDeutsch" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Media_resources_language_switcher_English(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/de/pressematerialien")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_link_text('English').click()
        try:
            if driver.find_element_by_tag_name('h1').text == "Media Resources":
               self.file1.writelines("SwitchToEnglish" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
            else:
               self.file1.writelines("SwitchToEnglish" + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        except:
            self.file1.writelines("SwitchToEnglish" + " " + "Exception occurred" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
        time.sleep(5)
        driver.get_screenshot_as_file( _init_.path1 + "SwitchToEnglish" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )


    def tearDown(self):
        self.file1.close()

if __name__ == "__main__":
    unittest.main()
