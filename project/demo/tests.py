import os
from django.test import TestCase
from selenium import webdriver

class SeleniumTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_admin_site(self):
        self.browser.get("http://localhost:8010/admin")
        self.assertIn('Iniciar sesión | Sitio de administración de Django',
                      self.browser.title)

    def tearDown(self):
        self.browser.close()
