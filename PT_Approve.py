import unittest
# import HtmlTestRunner
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/loginpage")    #run through cmd and to generate report we need this or else no need
from pages.purchase_tender_page import Purchase_Tender
#https://clever-brahmagupta-0d6b23.netlify.app
class purchase_tender_Test(unittest.TestCase):

    baseURL="https://testscm.digicollect.com/"
    email ="manager@testdigibar.com"
    password ="testdigibar123"
    # driver = webdriver.Firefox(executable_path="E:\geckodriver-v0.26.0-win64\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    prno="DIGICOLLECT1234"
    Bran="Test Digibar"
    trno="vandy@@K654"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_Purchase_tender(self):
        pt=Purchase_Tender(self.driver)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
        pt.login_page("manager@testdigibar.com","testdigibar123")
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="homepage", attachment_type=AttachmentType.PNG)
        pt.click_create_new()
        time.sleep(3)
        pt.click_foreign()
        time.sleep(3)
        pt.click_tr_no(self.trno)
        pt.click_pr_no()
        pt.click_branch()
        pt.click_dept()
        pt.click_Attention()
        pt.click_date()
        pt.click_currency()
        pt.click_authorised()
        pt.click_phone()
        # pt.click_address()
        # pt.click_Save()
        pt.click_same_as_billing()
        pt.click_product()
        pt.other_info()
        # pt.file_attach()
        pt.click_saveandsend()
        allure.attach(self.driver.get_screenshot_as_png(), name="sendapproval", attachment_type=AttachmentType.PNG)
        pt.approval()
        pt.click_send()
        pt.click_approve()
        pt.enter_note()
        pt.click_yes()
        pt.click_List()
        allure.attach(self.driver.get_screenshot_as_png(), name="listview", attachment_type=AttachmentType.PNG)
        pt.click_single()
        # pt.click_approved()
        pt.click_view_attach()
        allure.attach(self.driver.get_screenshot_as_png(), name="viewattach", attachment_type=AttachmentType.PNG)
        pt.click_close()
        pt.click_single()
        pt.click_list_delete()
        allure.attach(self.driver.get_screenshot_as_png(), name="delete", attachment_type=AttachmentType.PNG)
        #








if __name__=='__main__':
    unittest.main()