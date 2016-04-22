from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class SeleniumTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://gollum23-selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self):
        driver = self.browser
        driver.quit()

    def test_admin_site(self):
        driver = self.browser
        driver.get("http://gollum23-django:8010/admin/login")
        self.assertIn('Log in',
                      driver.title)
        driver.close()

    def test_admin_login_fail(self):
        driver = self.browser
        driver.get("http://gollum23-django:8010/admin/login")
        username_field = driver.find_element_by_id('id_username')
        password_field = driver.find_element_by_id('id_password')
        username_field.send_keys('gollum23')
        password_field.send_keys('platzi2016', Keys.ENTER)
        self.assertNotEqual('Site administration',
                            driver.find_element_by_tag_name('title')
                            )
        driver.close()

    def test_admin_login(self):
        driver = self.browser
        driver.get("http://gollum23-django:8010/admin/login")
        username_field = driver.find_element_by_id('id_username')
        password_field = driver.find_element_by_id('id_password')
        username_field.send_keys('gollum23')
        password_field.send_keys('platzo2016', Keys.ENTER)
        self.assertIn('Site administration',
                      driver.title)

        driver.close()
