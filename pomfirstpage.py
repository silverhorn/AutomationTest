"""All web elements located on the page fill-out-form with locators and methods"""

#Class name:

class Firstassessment():

# Constructor:

    def __init__(self, driver):
        self.driver = driver

# Element locators:

        self.FirstTextNameBox_id = "et_pb_contact_name_1"
        self.TextBoxMessage_id = "et_pb_contact_message_1"
        self.WrongCaptcha_name = "et_pb_contact_captcha_1"
        self.SubmitButton_xpath = "//div[@id='et_pb_contact_form_1']//button[@class='et_pb_contact_submit et_pb_button'][contains(text(),'Submit')]"
        self.TextBeforeAndAfterSubmit_class_name = "et_pb_contact_captcha_question"
        self.BoxCaptcha_css_selector = "input.input.et_pb_contact_captcha"
        self.SuccessMessage_css_selector = "div.et-pb-contact-message > p"

# Get the web elements and Actions on the web elements:

    def textBeforeAndAfterSubmit(self):
        beforesubmit = self.driver.find_element_by_class_name(self.TextBeforeAndAfterSubmit_class_name).text
        return beforesubmit
    def TextBoxName(self, name):
        self.driver.find_element_by_id(self.FirstTextNameBox_id).clear()
        self.driver.find_element_by_id(self.FirstTextNameBox_id).send_keys(name)
    def TextBoxMessage(self, message):
        self.driver.find_element_by_id(self.TextBoxMessage_id).clear()
        self.driver.find_element_by_id(self.TextBoxMessage_id).send_keys(message)
    def TextBoxWrongCaptcha(self, wrongnumber):
        self.driver.find_element_by_name(self.WrongCaptcha_name).clear()
        self.driver.find_element_by_name(self.WrongCaptcha_name).send_keys(wrongnumber)
    def SubmitButton(self):
        self.driver.find_element_by_xpath(self.SubmitButton_xpath).click()
    def BoxCapture(self, number):
        self.driver.find_element_by_css_selector(self.BoxCaptcha_css_selector).send_keys(number)
    def SuccessMessage(self):
        message = self.driver.find_element_by_css_selector(self.SuccessMessage_css_selector).text
        return message