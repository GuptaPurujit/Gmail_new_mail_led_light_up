from selenium import webdriver
import time
from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM

board = Arduino('COM3')

board.digital[12].mode = OUTPUT
def blink():
    board.digital[12].write(1)
def unblink():
    board.digital[12].write(0)

driver = webdriver.Chrome("C:/Users/Purujit/Desktop/facebook_login_script/chromedriver")

username = 'enter your username here'
password = 'enter your password here'
url = 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(url)
driver.find_element_by_name('identifier').send_keys(username + '\n')
# driver.find_element_by_id('identifierNext').click()
time.sleep(3)
driver.find_element_by_name('password').send_keys(password + '\n')
# driver.find_element_by_id('passwordNext').click()

time.sleep(10)

# unread = []
# unread.append("driver.find_element_by_xpath(\"//*[contains(@class,'zA zE')]\")")
# if len(unread) == 0:
#     print(False)
# elif len(unread) == 1:
#     print(True)
# else: 
#     print('Error')

unread = driver.find_element_by_xpath("//*[contains(@class,'zA zE')]")
while True:
    time.sleep(5)
    print(unread)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id=":4"]/div/div[1]/div[1]/div/div/div[5]/div').click()
    time.sleep(20)
    unread_temp = driver.find_element_by_xpath("//*[contains(@class,'zA zE')]")
    print(unread_temp)
    if unread_temp != unread:
        unread = unread_temp
        # print(True)
        blink()
        time.sleep(5)
        # unblink()
        continue
    print(False)
    continue
