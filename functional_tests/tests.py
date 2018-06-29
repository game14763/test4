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
    time.sleep(1)

    # He add in "Chicken" with 15% sugar
    inputbox = self.browser.find_element_by_id('id_food')
    inputbox.send_keys('Chicken')
    inputbox = self.browser.find_element_by_id('id_sugar')
    inputbox.send_keys('15')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    # He click on "Menu" to go to food menu
    start_menu = self.browser.find_element_by_tag_name('a')
    start_menu.click()

    # He see the tile and header Menu
    self.assertIn("Menu",self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Menu',header_text)

    # He see the food that he add in
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    self.assertIn('Food: Pork', [row.text for row in rows])
    self.assertIn('Sugar: 20 %', [row.text for row in rows])

    self.assertIn('Food: Chicken', [row.text for row in rows])
    self.assertIn('Sugar: 15 %', [row.text for row in rows])

    # He decide to delete "Pork" by clicking delete button below to it
    delete_food = self.browser.find_element_by_id('d1')
    delete_food.click()

    # He see that it has been delete and only Chicken is there
    # So he close the website and go to sleep
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    self.assertNotIn('Food: Pork', [row.text for row in rows])
    self.assertNotIn('Sugar: 20 %', [row.text for row in rows])

    self.assertIn('Food: Chicken', [row.text for row in rows])
    self.assertIn('Sugar: 15 %', [row.text for row in rows])

    time.sleep(3)
