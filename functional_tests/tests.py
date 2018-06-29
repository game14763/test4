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

  def test_can_start_food(self):

    # Al heard about a website that contain food menu and decide to visit
    self.browser.get(self.live_server_url)

    # He see the homepage and the title "Food"
    self.assertIn("Food",self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn("Food",header_text)

    # He see box for adding menu and sugar
    inputbox = self.browser.find_element_by_id('id_food')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own menu'
    )

    # He add in "Pork" with 20% sugar
    inputbox.send_keys('Pork')
    inputbox = self.browser.find_element_by_id('id_sugar')
    inputbox.send_keys('20')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He add in "Chicken" with 15% sugar
    inputbox = self.browser.find_element_by_id('id_food')
    inputbox.send_keys('Chicken')
    inputbox = self.browser.find_element_by_id('id_sugar')
    inputbox.send_keys('15')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He click on "Menu" to go to food menu
    start_menu = self.browser.find_element_by_tag_name('a')
    start_menu.click()

    # He see the tile and header Menu
    self.assertIn("Menu",self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Menu',header_text)

    # He see the food that he add in
    food = self.browser.find_element_by_id('f1').text
    self.assertIn('Pork',food)
    sugar = self.browser.find_element_by_id('s1').text
    self.assertIn('20',sugar)

    food = self.browser.find_element_by_id('f2').text
    self.assertIn('Chicken',food)
    sugar = self.browser.find_element_by_id('s2').text
    self.assertIn('15',sugar)

    # He decide to delete "Pork" by click delete next to it
    delete_food = self.browser.find_element_by_id('d1')
    delete_food.click()

    # He see that it has been delete and only Chicken is there close the website and go to sleep
    food = self.browser.find_element_by_id('f2').text
    self.assertIn('Chicken',food)
    sugar = self.browser.find_element_by_id('s2').text
    self.assertIn('15',sugar)

    food = self.browser.find_element_by_id('f1').text
    self.assertNotIn('Pork',food)
    sugar = self.browser.find_element_by_id('s1').text
    self.assertNotIn('20',sugar)
