import unittest
# import HtmlTestRunner
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/loginpage")    #run through cmd and to generate report we need this or else no need
from pages.Split_merge_page import Split_Merge_page
from pages.purchase_tender_page import Purchase_Tender
class Split_Merge_PT(unittest.TestCase):
    baseURL = "https://testscm.digicollect.com/"
    email = "manager@testdigibar.com"
    password = "testdigibar023"
    # driver = webdriver.Firefox(executable_path="E:\geckodriver-v0.26.0-win64\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    ptno = "vandy@Merge7"
    Bran = "Test Digibar"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_SM_PT(self):
        sm=Split_Merge_page(self.driver)
        time.sleep(3)
        pt = Purchase_Tender(self.driver)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
        sm.login_page("manager@testdigibar.com", "testdigibar123")
        allure.attach(self.driver.get_screenshot_as_png(), name="homepage", attachment_type=AttachmentType.PNG)
        time.sleep(10)
        pt.click_List()
        pt.PT_created()
        pt.click_split()
        allure.attach(self.driver.get_screenshot_as_png(), name="split", attachment_type=AttachmentType.PNG)
        pt.click_plus()
        pt.click_proceed()
        pt.split_plus()
        pt.click_next()
        pt.split_After_plus()
        pt.After_plus_split()
        time.sleep(10)
        pt.click_List()
        pt.second_split()
        pt.click_merge()
        allure.attach(self.driver.get_screenshot_as_png(), name="merge", attachment_type=AttachmentType.PNG)
        pt.click_checkbox()
        pt.merge_click()
        allure.attach(self.driver.get_screenshot_as_png(), name="merge_request", attachment_type=AttachmentType.PNG)
        pt.click_foreign()
        pt.click_pt_no(self.ptno)
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
        # pt.click_product()
        pt.other_info()
        # pt.file_attach()
        # pt.click_saveandsend()
        # allure.attach(self.driver.get_screenshot_as_png(), name="sendapproval", attachment_type=AttachmentType.PNG)
        pt.click_saveandview()
        pt.click_List()
        pt.merged()

