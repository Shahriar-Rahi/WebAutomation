from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path='E:\Rahi User Data of Windows\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


browser.get("http://www.facebook.com")
  
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
submit   = browser.find_element_by_id("submit")
  
username.send_keys("me")
password.send_keys("mykewlpass")
  

submit.click()
  

wait = WebDriverWait( browser, 5 )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)