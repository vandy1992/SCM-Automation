import unittest
# import HtmlTestRunner
import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/loginpage")    #run through cmd and to generate report we need this or else no need
from pages.home.login_page import LoginPage
from selenium.webdriver.common.keys import Keys

#https://wizardly-pare-d41d3f.netlify.app/#

class PR_createnew(unittest.TestCase):

    baseURL="https://testscm.digicollect.com/"
    email ="manager@testdigibar.com"
    password ="testdigibar023"
    driver = webdriver.Firefox(executable_path="E:\geckodriver-v0.26.0-win64\geckodriver.exe")
    # driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    prno="Dkjsl@01212"
    Bran="Test Digibar"

    # @allure.severity(allure.severity_level.NORMAL)
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
    @allure.severity(allure.severity_level.CRITICAL)
    def test_PR(self):
        lp=LoginPage(self.driver)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
        # self.driver.save_screenshot("C:..\\Screenshoot\\loginpage.png")
        lp.login_page("manager@testdigibar.com","testdigibar123")
        time.sleep(10)
        allure.attach(self.driver.get_screenshot_as_png(), name="homepage", attachment_type=AttachmentType.PNG)
        # self.driver.save_screenshot("C:..\\Screenshoot\\homepage.png")
        lp.click_IMS()
        time.sleep(15)
        allure.attach(self.driver.get_screenshot_as_png(), name="createnew", attachment_type=AttachmentType.PNG)
        # self.driver.save_screenshot("C:..\\Screenshoot\\createnew.png")
        lp.click_foreign()
        lp.click_pr_no(self.prno)
        lp.click_branch()
        lp.click_dept()
        lp.click_Attention()
        lp.click_request()
        lp.click_date()
        lp.click_currency()
        lp.click_authorised()
        lp.click_phone()
        # lp.click_address()
        # lp.click_Save()
        lp.click_same_as_billing()
        lp.click_vendor()
        lp.click_product()
        lp.other_info()
        # lp.choose_file()
        # lp.click_saveandsend()
        lp.click_saveandview()
        # lp.approval()
        # lp.click_send()
        # lp.click_List()
        # allure.attach(self.driver.get_screenshot_as_png(), name="listview", attachment_type=AttachmentType.PNG)
        # # self.driver.save_screenshot("C:..\\Screenshoot\\listview.png")
        # lp.click_single()
        # lp.click_view_attach()
        # allure.attach(self.driver.get_screenshot_as_png(), name="viewattach", attachment_type=AttachmentType.PNG)
        # # self.driver.save_screenshot("C:..\\Screenshoot\\viewattach.png")
        # lp.click_close()
        # lp.click_single()
        # lp.click_list_delete()
        # allure.attach(self.driver.get_screenshot_as_png(), name="delete", attachment_type=AttachmentType.PNG)
        # self.driver.save_screenshot("C:..\\Screenshoot\\delete.png")

    # @classmethod
    # def tearDownClass(cls):
    #    cls.driver.close()

if __name__=='__main__':
    unittest.main()



