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

class Split_Merge_test(unittest.TestCase):
    baseURL = "https://testscm.digicollect.com/"
    email = "manager@testdigibar.com"
    password = "testdigibar023"
    # driver = webdriver.Firefox(executable_path="E:\geckodriver-v0.26.0-win64\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    prno = "vandy1824"
    Bran = "Test Digibar"
    PRNO = "vandy@merge11"

    # @allure.severity(allure.severity_level.BLOCKER)
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @allure.severity(allure.severity_level.MINOR)
    def test_PR_SM(self):
        sm=Split_Merge_page(self.driver)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
        sm.login_page("manager@testdigibar.com","testdigibar123")
        allure.attach(self.driver.get_screenshot_as_png(), name="homepage", attachment_type=AttachmentType.PNG)
        time.sleep(10)
        sm.click_List()
        sm.click_single()
        sm.click_edit()
        sm.click_saveandview()
        time.sleep(5)
        sm.click_split()
        allure.attach(self.driver.get_screenshot_as_png(), name="split", attachment_type=AttachmentType.PNG)
        sm.click_plus()
        sm.click_proceed()
        sm.split_plus()
        sm.click_next()
        sm.split_After_plus()
        sm.After_plus_split()
        time.sleep(10)
        sm.second_split()
        sm.click_merge()
        allure.attach(self.driver.get_screenshot_as_png(), name="merge", attachment_type=AttachmentType.PNG)
        sm.click_checkbox()
        sm.merge_click()
        allure.attach(self.driver.get_screenshot_as_png(), name="merge_request", attachment_type=AttachmentType.PNG)
        sm.click_foreign()
        sm.click_pr_no_merge(self.PRNO)
        sm.click_branch()
        sm.click_dept()
        sm.click_Attention()
        sm.click_request()
        sm.click_date()
        sm.click_currency()
        sm.click_authorised()
        sm.click_phone()
        # sm.click_address()
        # sm.click_Save()
        sm.click_same_as_billing()
        sm.click_vendor()
        sm.other_info()
        sm.click_saveandview()
        sm.click_List()
        sm.merged()

