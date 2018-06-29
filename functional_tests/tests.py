from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()
  # Al heard about a website that contain food menu and decide to visit
  # He see the homepage and the title "Food"
  # He see box for adding menu and sugar
  # He add in "Pork" with 20% sugar
  # He add in "Chicken" with 15% sugar
  # He click on "Menu" to go to food menu
  # He see the food that he add in
  # He decide to delete "Pork" by click delete next to it
  # He see that it has been delete close the website and go to sleep
