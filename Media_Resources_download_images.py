import unittest
import csv
import time
import _init_
from datetime import datetime
from selenium import webdriver



class Media_Resources_Download_Images(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(_init_.path3)
        self.file1 = open(_init_.path2 + "Testcaseresults_media_resources.csv", "a+")

    def test_Media_resources_download_logo(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/media-resources")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.execute_script( "window.scrollTo(0,700)" )
        try:
            driver.find_element_by_link_text('DOWNLOAD').click()
            self.file1.writelines("DownloadLogo" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        except:
            self.file1.writelines("DownloadLogo" + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        time.sleep(2)


        driver.get_screenshot_as_file(_init_.path1 + "DownloadLogo" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def test_Media_resources_Download_FoundersImage(self):

        driver = self.driver
        driver.set_page_load_timeout( 10 )
        driver.get( "https://www.xeneta.com/media-resources" )
        driver.maximize_window()
        driver.execute_script( "window.scrollTo(0,1200)" )
        driver.implicitly_wait( 5 )
        driver.find_element_by_link_text('Image of Founders').click()
        time.sleep(2)
        try:
            driver.find_element_by_link_text('Download full resolution').click()
            self.file1.writelines("DownloadFoundersImage" + " " + "Passed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
            time.sleep(5)

        except:
            self.file1.writelines("DownloadFoundersImage" + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )

        time.sleep( 2 )

        driver.get_screenshot_as_file(_init_.path1 + "DownloadFoundersImage" + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )


    def tearDown(self):
        self.file1.close()

if __name__ == "__main__":
    unittest.main()
