import unittest
import csv
from datetime import datetime
from selenium import webdriver
import _init_



class Xeneta_RequestDemo(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome( _init_.path3 )
        self.file = open( _init_.path + "TestData_Elements_request_demo_Text_Validation.CSV", "r" )
        self.file1 = open( _init_.path2 + "Testcaseresults_request_demo.csv", "a+" )

    def test_Request_Demo_text_validation(self):

        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.get("https://www.xeneta.com/test-request-xeneta-demo")
        driver.maximize_window()
        filedata = csv.reader(self.file, delimiter=';')
        print(filedata)
        for line in filedata:
            if line[1] == "xpath":
                x = driver.find_element_by_xpath(line[2]).get_attribute(line[3])
                if x == line[4]:
                    self.file1.writelines(line[0] + " " + "Passed" + " " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                    print(x)
                else:
                    self.file1.writelines(line[0] + " " + "Failed" + " " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' +'\n' )
                    print(x)
            elif line[1] == "id":
                x = driver.find_element_by_id(line[2]).text
                if x == line[3]:
                    self.file1.writelines(line[0] + " " + "Passed" + " " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')
                    print(x)
                else:
                    self.file1.writelines(line[0] + " " + "Failed" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')
                    print(x)
            driver.get_screenshot_as_file( _init_.path1 + line[0] + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )

    def tearDown(self):
        self.file.close()
        self.file1.close()

if __name__ == "__main__":
    unittest.main()
