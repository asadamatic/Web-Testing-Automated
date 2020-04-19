import unittest
from RegistrationForm import *


class Test(unittest.TestCase):

    def test_case_1(self):

        """ Test case to identify presence of expected elements on registration page """

        self.assertTrue(verifyExpectedElements())


    def test_case_2(self):

        """ Test case for terms of service link redirection """

        expectedUrl = 'https://www.lambdatest.com/terms-of-service'

        expectedTitle = 'Terms of Service - LambdaTest'

        pageInfo = termsLinkRedirection()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle)

    def test_case_3(self):

        """ Test case for privacy policy link redirection """

        expectedUrl = 'https://www.lambdatest.com/privacy'

        expectedTitle = 'Privacy Policy | LambdaTest'

        pageInfo = privacyLinkRedirection()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle)

    def test_case_4(self):

        """ Test case for login link redirection """

        expectedUrl = 'https://accounts.lambdatest.com/login'

        expectedTitle = 'Login - LambdaTest'

        pageInfo = loginLinkRedirection()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle)

    def test_case_5(self):

        """ Test case for logo landing page redirection """

        expectedUrl = 'https://www.lambdatest.com/'

        expectedTitle = 'Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest'

        pageInfo = logoRedirection()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle) 

    def test_case_6(self):

        """ Test case for registration with valid input data """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithValidInput()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle) 


    def test_case_7(self):

        """ Test case for registration with empty full name field and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithEmptyFullName()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 


    def test_case_8(self):

        """ Test case for registration with empty email field and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithEmptyEmail()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 

    def test_case_9(self):

        """ Test case for registration with invalid email and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithInvalidEmail()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 

    def test_case_9_1(self): #including 9 in name to order cases correctly in execution

        """ Test case for registration with already registered email and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithAlreadyRegisteredEmail()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 

    
    def test_case_round_9_2(self):

        """ Test case for registration with empty password field and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithEmptyPassword()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 


    def test_case_9_3(self):

        """ Test case for registration with invalid password and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithInvalidPassword()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 


    def test_case_9_4(self):

        """ Test case for registration with empty phone field and valid data for rest of the fields """

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithEmptyPhone()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 


    def test_case_9_5(self):

        """ Test case for registration with invalid phone number and valid data for rest of the fields"""

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithInvalidPhone()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertNotEqual(expectedUrl, actualUrl)

        self.assertNotEqual(expectedTitle, actualTitle) 


    def test_case_9_6(self):

        """ Test case for registration with empty company name field and valid data for rest of the fields"""

        expectedUrl = 'https://accounts.lambdatest.com/email/verify'

        expectedTitle = 'Verify Your Email Address - LambdaTest'

        pageInfo = registrationWithEmptyCompanyName()

        actualUrl = pageInfo[0]

        actualTitle = pageInfo[1]

        self.assertEqual(expectedUrl, actualUrl)

        self.assertEqual(expectedTitle, actualTitle) 

    def tearDown(self):

        closeBrowser()


if __name__ == '__main__':

    unittest.main()

"""
Hi there, I was just following your tutorial, this one
https://www.lambdatest.com/blog/selenium-java-tutorial-automation-testing-of-user-signup-form/
and I'm facing issue with the 'alert' 'please fill out this field'
and the xpath that was provided in the tutorial does not work even with modifications.
Please help me solve the issue
"""