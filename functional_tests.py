from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
# Al heard about a website that contain food menu and decide to visit
# he see the homepage and the title "Food"
# he see box for adding menu and sugar
# he add in "Pork" with 20% sugar
# he add in "Chicken" with 15% sugar
