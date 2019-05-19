from selenium import webdriver
import time
import unittest
from pomfirstpage import Firstassessmen
"""
This class consist of tests. It inherits unittest.TestCase class. Also consist setUp and tearDown methods which are 
used to set up test with necessarily preconditions which will be executed before each test and to set up conditions 
which will be executed after each test
"""


class CheckTest(unittest.TestCase): #Class name
    baseURL = "https://www.ultimateqa.com/filling-out-forms/" # Storing the URL into var
    basePath = "C:/Python37-32/automation/driver/chromedriver.exe" # Storing the path to chrome driver into var
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(self.basePath)
        self.driver.implicitly_wait(5) # Setting implicitly wait to 5 sec
        self.driver.maximize_window() # Maximizing the window after launching the Chrome browser


    def tearDown(self):
        self.driver.quit()

    """ This test will fill out form but in the 'Result' field will pass negative 1 which will result in the error msg. 
    At the end it verifies that sum expression before clicking on the 'Submit' button is different that sum expression 
    after clicking on the 'Submit button' """

    def test_check_valid(self):
        driver = self.driver
        driver.get(self.baseURL) # Going to the desirable URL

        FirstCheck = Firstassessment(driver)
        TextBeforeSubmit = FirstCheck.textBeforeAndAfterSubmit() # Getting the sum expression text
        print(TextBeforeSubmit) # Printing the sum expression text into console
        FirstCheck.TextBoxName("Test") # Filling the Name field with "Text name"
        FirstCheck.TextBoxMessage("Test") # Filling the Message field with "Text message"
        FirstCheck.TextBoxWrongCaptcha("-1") # Filling the Result field with negative 1
        FirstCheck.SubmitButton() #Clicking on the Submit button
        TextAfterSubmit = FirstCheck.textBeforeAndAfterSubmit() # Getting the sum expression text after submit
        print(TextAfterSubmit) # Printing the sum expression text into console after submit

        if TextBeforeSubmit != TextAfterSubmit: # Verification (If stings aren't equal)
            print("Numbers have changed") # Printing verification
        else:
            print("Numbers have not changed")
        time.sleep(2)


    """This test will fill out form and it will fill out correct 'Result' which will result showing the success message
     to the user. At the end it verifies that success msg is equal to 'Success'"""


    def test_check_validtwo(self):
        driver = self.driver
        driver.get(self.baseURL) # Going to the desirable URL

        SecondCheck = Firstassessment(driver)

        textBeforeSubmitForm = SecondCheck.textBeforeAndAfterSubmit() # Getting the sum expression text after submit
        print(textBeforeSubmitForm) # Printing the sum expression text before submit

        captcha_list = textBeforeSubmitForm.split(' ') # Making list of printed sum expression text
        print(captcha_list) # Printing list of sum expression text
        firstnumberfromlist = captcha_list[0] # Making a string of the first element from the list of sum expression text
        print(firstnumberfromlist) # Printing a string of the first element from the list of sum expression text
        firstnumberfromlist = int(firstnumberfromlist)# Making integer of the first element from the list of sum expression text
        print(firstnumberfromlist) # Printing integer  of the first element from the list of sum expression text
        secondnumberfromlist = captcha_list[2] # Making a string of the third element from the list of sum expression text
        print(secondnumberfromlist) # Printing a string of the third element from the list of sum expression text
        secondnumberfromlist = int(secondnumberfromlist) # Making integer of the third element from the list of sum expression text
        print(secondnumberfromlist) # Printing integer  of the third element from the list of sum expression text
        captchacorectnumber = firstnumberfromlist + secondnumberfromlist # Sum of the first and third element from list
        print(captchacorectnumber) # Printing sum of the first and third element from list

        SecondCheck.TextBoxName("Test") # Filling the Name field with "Text name"
        SecondCheck.TextBoxMessage("Test") # Filling the Message field with "Text message"

        SecondCheck.BoxCapture(captchacorectnumber) # Filling correct number into captcha box

        SecondCheck.SubmitButton() # Clicking on the Submit button

        message = SecondCheck.SuccessMessage() # Verifying that success message is "Success"
        print(message) #Printing "Success" message
        time.sleep(4)


if __name__ == '__main__':
    unittest.main()