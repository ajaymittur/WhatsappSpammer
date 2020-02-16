from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Required only when chain of actions is to be performed
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

message = input('Enter the spam to bombard the group with: ')
sendNTimes = int(input('No. of times the message should be sent: '))
group = input('Finally enter the group/contact you want to spam: ')
input('Scan the QR code and sign in when the site loads. (HIT ANY KEY)')

# Initialize chromedriver and open whatsapp web
chrome = webdriver.Chrome()
chrome.get('https://web.whatsapp.com/')

try:
    classGroup = WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.XPATH, f'//span[@title=\'{group}\']'))) # Wait till chats page loads and classGroup chat is found in DOM
    classGroup.click() # Click the class group chat
except:
    chrome.close()
    sys.exit('Group not found!')

# Can be used when chain of actions is to be performed
# ActionChains(chrome).click(classGroup).perform()

# messageBox = chrome.find_element_by_xpath('//div[@class=\'_3u328 copyable-text selectable-text\']') # Find the message box 
messageBox = chrome.find_element_by_xpath('//div[@data-tab=\'1\' and contains(@class, \'copyable-text selectable-text\') and @dir=\'ltr\']') # Find the message box 

choice = input('You ready to go?!?!?! (Y/N)')
if choice.lower() == 'y':
    # Send the message the specified number of times
    for i in range(sendNTimes):
        messageBox.send_keys(message)
        messageBox.send_keys(Keys.RETURN)
        print("Message Sent: %s Number Of Times: %d" % (message, i + 1))

chrome.close()