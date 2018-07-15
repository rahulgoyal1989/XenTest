import unittest
import logging
import csv
from datetime import datetime
from selenium import webdriver
import _init_

class Xeneta_RequestDemo_webform_submit(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome( _init_.path3 )
        logging.info(f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"Chrome Driver Initialized")
        self.file = open( _init_.path + "TestData_Elements_request_demo_webform_submit.CSV", "r" )
        logging.info( f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"TestData_Elements_request_demo_webform_submit.CSV" + " " + "file is opened")
        self.file1 = open( _init_.path2 + "Testcaseresults_request_demo.csv", "a+" )
        logging.info(f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"Testcaseresults_request_demo" + " " + "file is opened" )


    def test_Request_Demo_webform_submit(self):
        filedata = csv.reader(self.file, delimiter=';')
        logging.info(f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"Reading each line in Input data file")
        for line in filedata:
            driver = self.driver
            driver.set_page_load_timeout(10)
            driver.get("https://www.xeneta.com/test-request-xeneta-demo")
            driver.maximize_window()
            logging.info(f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"Webpage opened in chrome" )
            driver.implicitly_wait(5)
            driver.find_element_by_name("firstname").send_keys(line[1])
            driver.find_element_by_name("lastname").send_keys(line[2])
            driver.find_element_by_name("company").send_keys(line[3])
            driver.find_element_by_name("jobtitle").send_keys(line[4])
            driver.find_element_by_name("email").send_keys(line[5])
            driver.find_element_by_name("direct_phone__c").send_keys(line[6])
            driver.find_element_by_name("type_of_prospect").send_keys(line[7])
            driver.find_element_by_name("teu_shipped_anually").send_keys( line[8] )
            driver.find_element_by_name("persona_2018").send_keys( line[9])
            if line[10] == "Yes":
                driver.find_element_by_name("xeneta_industry_blog_instant_email_subscription").click()
            driver.find_element_by_xpath("//input[@type = 'submit']").click()
            driver.implicitly_wait(15)
            try:
                if line[11] == "Yes":

                    submitsuccessresponse = driver.find_element_by_id("hs_form_target_widget_1511361239949").text
                    print(submitsuccessresponse)
                    if submitsuccessresponse == "Thanks for submitting the form.":
                        self.file1.writelines(line[0] + " " + "Passed" +" " + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                    else:
                        self.file1.writelines(line[0]+" "+"Failed" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n')

                else:
                    submitfailureresponse = driver.find_element_by_xpath("//div[@class = 'hs_error_rollup']/ul[1]/li[1]/label").get_attribute("innerHTML")
                    print( submitfailureresponse )
                    if submitfailureresponse == "Please complete all required fields.":
                        self.file1.writelines( line[0] + " " + "Passed" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
                    else:
                        self.file1.writelines( line[0] + " " + "Failed" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )
            except:
                self.file1.writelines( line[0] + " " + "Exception occurred" +" " +f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + '\n' )


            logging.info(f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + "-"+"Test Executed" )
            driver.get_screenshot_as_file( _init_.path1 + line[0] + "_" + f'{datetime.now():%Y-%m-%d %H-%M-%S%z}' + ".png" )




    def tearDown(self):
        self.file.close()
        self.file1.close()

if __name__ == "__main__":
    unittest.main()
