import time
from selenium.webdriver.common.keys import Keys
class Purchase_Tender():
    #Locators of all the web element
    email_xpath="emailaddress"
    password_name="password"
    signin_xpath="//button[@class='btn btn-block btn-gradient fuse-ripple-ready']"
    forgot_password_xpath="//small[contains(text(),'Forgot your password?')]"
    signUp_xpth="//b[contains(text(),'Sign Up')]"

    def __init__(self,driver):
        self.driver=driver
    def setUserEmail(self,email):
        self.driver.find_element_by_id(self.email_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_name(self.password_name).send_keys(password)
    def clickSignin(self):
        self.driver.find_element_by_xpath(self.signin_xpath).click()
    def login_page(self,email,password):
        self.setUserEmail(email)
        self.setPassword(password)
        self.clickSignin()


    #purchase request
    ims="//span[@class='font-weight-bold text-white'][contains(text(),'IMS')]"
    purchase="/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    purchase_tender="/html/body/div[1]/div/main/div[1]/div/div[2]/div/ul/li[4]/ul/li[1]/ul/li[2]/a"
    create_new="//ul[@class='dropdown-menu closeMenu scm-submenu subMenuScroll subFlexScroll show']//a[@class='dropdown-sub-item nav-link'][contains(text(),'Create New')]"
    list_view="//ul[@class='dropdown-menu closeMenu scm-submenu subMenuScroll subFlexScroll show']//a[@class='dropdown-sub-item nav-link'][contains(text(),'List View')]"
    # prno="DIGICOLLECT1234"
    branch = "//span[@class='multiselect__placeholder'][contains(text(),'Select Branch')]"
    testdigibar = "//span[contains(text(),'Test Digibar')]"
    department = "//input[@name='department']"
    attention = "//input[@name='attention']"
    requested = "//span[contains(text(),'Select Requested By')]"
    expected_delivary_date = "//input[@name='date']"
    date = "//td[@class='cell next-month'][contains(text(),'4')]"
    apply = "//button[@class='mx-datepicker-btn mx-datepicker-btn-confirm']"
    currency = "//input[@name='currency']"
    tend_no="//input[@name='tr_no']"


    def click_create_new(self):
        self.driver.find_element_by_xpath(self.ims).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.purchase).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.purchase_tender).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.create_new).click()
        time.sleep(6)
    def click_List(self):
        self.driver.find_element_by_xpath(self.ims).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.purchase).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.purchase_tender).click()
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div/div[2]/div/ul/li[4]/ul/li[1]/ul/li[2]/ul/li[1]/a").click()
        time.sleep(7)


    # Create New
    local_vendor = "//span[contains(text(),'Local Vendor')]"
    foreigen_vender = "//span[contains(text(),'Foreign Vendor')]"

    def cilck_local(self):
        self.driver.find_element_by_xpath(self.local_vendor).click()
    def click_foreign(self):
        self.driver.find_element_by_xpath(self.foreigen_vender).click()
        time.sleep(4)

    def click_tr_no(self,trno):
        self.driver.find_element_by_xpath(self.tend_no).send_keys(trno)
        time.sleep(4)

    def click_pr_no(self):
        pr_no=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div[1]").click()
        pr_no=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div[3]/ul/li[5]/span/span").click()
        time.sleep(4)
    def click_branch(self):
        brancno = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[2]/div[1]/div[1]/div/div[2]")
        brancno.click()
        brancno = self.driver.find_element_by_xpath("//span[contains(text(),'Test Digibar')]")
        brancno.click()
        time.sleep(3)
    def click_dept(self):
        dept = self.driver.find_element_by_xpath("//span[contains(text(),'Select Department')]")
        dept.click()
        time.sleep(3)
        dept = self.driver.find_element_by_xpath("//span[contains(text(),'Default')]")
        dept.click()
        time.sleep(3)
    def click_Attention(self):
        atten = self.driver.find_element_by_xpath("//span[contains(text(),'Select Attention')]")
        atten.click()
        time.sleep(3)
        atten = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/span")
        atten.click()

    # def click_request(self):
    #     requ = self.driver.find_element_by_xpath("//span[contains(text(),'Select Requested By')]")
    #     requ.click()
    #     time.sleep(3)
    #     requ = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/span")
    #     requ.click()

    def click_date(self):
        exp_date = self.driver.find_element_by_xpath(self.expected_delivary_date)
        exp_date.click()
        time.sleep(3)
        exp_date = self.driver.find_element_by_xpath(self.date)
        exp_date.click()
        time.sleep(3)
        exp_date = self.driver.find_element_by_xpath(self.apply)
        exp_date.click()

    def click_currency(self):
        currency = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[5]/div/div[1]/div/div[2]")
        currency.click()
        time.sleep(3)
        currency = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/div[2]/div[5]/div/div[1]/div/div[3]/ul/li[2]/span").click()
        # currency.click()
        time.sleep(3)

    def click_authorised(self):
        autorized_person = self.driver.find_element_by_xpath("(//div[@class='multiselect__tags'])[6]")
        autorized_person.click()
        time.sleep(3)
        autorized_person = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/span/div")
        autorized_person.click()
        time.sleep(3)

    def click_phone(self):
        cust_phone = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/div[1]/div/input")
        cust_phone.click()
        time.sleep(3)
        cust_phone.send_keys("9987642277")
        cust_phone.click()
        time.sleep(3)

    def click_address(self):
        address=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[5]/div[4]/div/div[2]")
        address.click()
        time.sleep(5)
        address=self.driver.find_element_by_xpath("//span[contains(text(),'Factory')]").click()
        time.sleep(5)
        address=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div/input")
        time.sleep(3)
        address.send_keys("Bangalore Railway")
        time.sleep(3)
        address.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        address.send_keys(Keys.ENTER)
        time.sleep(3)
    def click_Save(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div/div/div[2]/div/div[2]/div[2]/button").click()
    def click_Cancel(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div/div/div[2]/div/div[2]/div[2]/a").click()

    def click_same_as_billing(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/label/span[2]").click()

    def click_product(self):
        product_code = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tbody/tr/td[2]/div/div/input")
        product_code.click()
        time.sleep(3)
        product_code = self.driver.find_element_by_xpath("//span[contains(text(),'cafe_latta')]")
        product_code.click()
        time.sleep(3)
        lot_no=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tbody/tr/td[4]/input")
        lot_no.send_keys("5")
        time.sleep(3)
        # product_name=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[8]/div[2]/table/tbody/tr/td[3]/div/div/input")
        # product_name.click()
        # time.sleep(3)
        # product_name=self.driver.find_element_by_xpath("/html/body/div[12]/div[1]/div[1]/ul/li[5]/span")
        # product_name.click()
        # time.sleep(3)
        measure=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tbody/tr/td[5]/input")
        measure.click()
        time.sleep(3)
        measure.send_keys("1")
        um=self.driver.find_element_by_xpath("//input[@placeholder='Select UM']")
        um.click()
        time.sleep(3)
        um=self.driver.find_element_by_xpath("//span[contains(text(),'Grams')]").click()
        time.sleep(3)
        targeted_price=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tbody/tr/td[7]/input")
        targeted_price.click()
        time.sleep(3)
        targeted_price.send_keys("0")
        order=self.driver.find_element_by_xpath("//input[@placeholder='Enter Item Quantity']")
        order.click()
        time.sleep(3)
        order.send_keys("0")
        time.sleep(3)
        note=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tbody/tr/td[9]/input")
        note.send_keys("product should be deliverd on time" )
    def other_info(self):
        payment=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[8]/div[2]/div[1]/div/div/div/div[2]")
        payment.click()
        time.sleep(3)
        payment=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[8]/div[2]/div[1]/div/div/div/div[3]/ul/li[3]/span/span")
        payment.click()
        enter_text=self.driver.find_element_by_xpath("//textarea[@placeholder='Enter Other Instructions']").send_keys("Payment must done with in the time")
        time.sleep(3)
        # enter_text.send_keys("Payment must done with in the time")

        #attachment File
    def file_attach(self):
        file=self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[9]/div[2]/div[1]/div/label")
        # file.click()
        # time.sleep(15)
        file.send_keys("C:..\\file\\CRM_Manual_ Document.pdf" )
        time.sleep(20)

    def click_cancel(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[11]/a").click()
        time.sleep(3)
    def click_saveandsend(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-success text-white btn-smm ml-3']").click()
        time.sleep(7)
    def click_saveandview(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[10]/button[1]").click()
        time.sleep(7)
    def approval(self):
        purchase=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]")
        purchase.click()
        time.sleep(3)
        purchase=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[3]/ul/li[4]/span/div")
        purchase.click()
        time.sleep(3)
        c_c=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]")
        c_c.click()
        time.sleep(3)
        c_c=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[3]/ul/li[1]/span/div")
        c_c.click()
        time.sleep(3)
        notes=self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/textarea")
        notes.send_keys("please approve the sent Purchase request")
        time.sleep(5)
    def click_cancel_send(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[9]/div[1]/div/div[2]/div/div[2]/div[2]/a").click()
        time.sleep(3)
    def click_send(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/div[2]/button").click()
        time.sleep(10)
    def click_approve(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div[2]/button[2]").click()
        time.sleep(5)
    # def click_reject(self):
    #     self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div[2]/button[2]").click()

    def enter_note(self):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Enter Notes']").send_keys("we accepted the tender and approved for further process")
        time.sleep(5)
    def click_yes(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[5]/div[1]/div/div[2]/div/div[2]/button").click()
        time.sleep(10)
    # def click_approved(self):
    #     self.driver.find_element_by_xpath("//tr[1]//td[8]//button[1]//span[1]").click()
    #     time.sleep(5)
    def click_single(self):
        self.driver.find_element_by_xpath("//tr[1]//td[7]//button[1]").click()
        time.sleep(5)
    def click_view_attach(self):
        self.driver.find_element_by_xpath("//tr[1]//td[9]//span[1]//button[1]//i[1]").click()
        time.sleep(5)
    def click_edit(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[9]/span/button[2]/i").click()
        time.sleep(5)
    def click_delete(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[9]/span/button[3]/i").click()
        time.sleep(5)
    def click_close(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button").click()
        time.sleep(6)
    def click_list_delete(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[9]/span/button[3]/i").click()
        time.sleep(6)

    def PT_created(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[2]/div").click()
        time.sleep(8)

    def click_split(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Split')]").click()
        time.sleep(8)

    def click_plus(self):
        self.driver.find_element_by_xpath("//*[@id='SplitSelection0']/div/div[4]/div[2]/span[2]/i").click()
        time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@id="main"]/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[1]").click()
        # time.sleep(3)

    def click_proceed(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'PROCEED')]").click()
        time.sleep(13)

    def split_plus(self):
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[2]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[2]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[2]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[2]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[2]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)

    def click_next(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'NEXT')]").click()
        time.sleep(8)

    def split_After_plus(self):
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[3]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[3]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[3]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[3]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='MoveProdcuts1']/div/div/div[3]/table/tbody/tr/td[3]/div/span[2]/i").click()
        time.sleep(3)

    def After_plus_split(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/button").click()
        time.sleep(3)
    # def edit_click(self):
    #     self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[3]/td[8]/span/button[2]/i").click()
    #     time.sleep(3)
    # def click_save_view(self):
    #     self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/div/div/div[11]/button[1]").click()
    #     time.sleep(3)

    def second_split(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[2]/td[2]/div").click()
        time.sleep(8)
    def click_merge(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Merge')]").click()
        time.sleep(8)
    def click_checkbox(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[1]/div/label/span[2]").click()
        time.sleep(8)
        # self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[3]/td[1]/div/label/span[2]").click()
        # time.sleep(8)
    def merge_click(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[4]/div/div/div[2]/div/div[2]/div[2]/button").click()
        time.sleep(8)
    def click_pt_no(self,ptno):
        self.driver.find_element_by_xpath(self.tend_no).send_keys(ptno)
        time.sleep(4)

    def merged(self):
        self.driver.find_element_by_xpath("//*[@id='main']/div[2]/div/section/div/div[1]/div/div/div[1]/div/div/table/tbody/tr[1]/td[2]/div").click()
        time.sleep(8)





