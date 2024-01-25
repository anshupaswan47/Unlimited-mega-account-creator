from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from mailtm import Email
import re


Link1 = "https://mega.nz/register"
chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=Link1)

fname= '//*[@id="register-firstname-registerpage2"]'
lname= '//*[@id="register-lastname-registerpage2"]'
emailpath = '//*[@id="register-email-registerpage2"]'
passpath = '//*[@id="register-password-registerpage2"]'
confirmpass = '//*[@id="register-password-registerpage3"]'
agree1 = '//*[@id="register_form"]/div[8]/div[1]/input'
agree2 = '//*[@id="register-check-registerpage2"]'
createacc = '//*[@id="register_form"]/button/span'

test = Email()
test.register()
email_address = str(test.address)
password = '@Megapass'
first_name = 'Mr'
last_name = 'Rider'

def listener(message):
    for i in range(2): 
        try:
            msg = "Content: " + message['text'] if message['text'] else message['html']
            url_match = re.search(r'https://mega\.nz/#confirm[^\s]+', msg)
            if url_match:
                mega_url = url_match.group(0)
                with open('mega_url.txt', 'w') as file:
                    file.write(mega_url)
                    print("URL Updated")
                break
        except:
            pass
        
ass = '//*[@id="bodyel"]/section[5]/div[14]/header/i[2]pp'
def WebsiteStart():
    sleep(6)
    print("1st Proccess Started !")

    try:
        driver.find_element(by=By.XPATH,value=fname).send_keys(first_name)
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=lname).send_keys(last_name)
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=emailpath).send_keys(email_address)
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=passpath).send_keys(password)
        
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=confirmpass).send_keys(password)
    except:
        pass
    try:
        
        driver.find_element(by=By.XPATH,value=agree1).click()
    except:
        pass
    try:
        
        driver.find_element(by=By.XPATH,value=agree2).click()
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=createacc).click()
        if driver.find_element(by=By.XPATH,value=ass):
            print("1st Proccess Done")
        else:
            WebsiteStart()
    except:
        pass
        

confirmpasspath = '//*[@id="login-password2"]'
confirmaccpath = '//*[@id="login_form"]/button/span'

def confirmtab():
    try:
        print("second Proeccess Started")
        sleep(1)
        driver.find_element(by=By.XPATH,value=confirmpasspath).send_keys(password)
    except:
        pass
    try:
        sleep(1)
        driver.find_element(by=By.XPATH,value=confirmaccpath).click()
        print("second Proecces Done ")
    except:
        pass

 # -----------run---------------
WebsiteStart()

try:
    sleep(5)
    test.start(listener)
finally:
    test.stop()
try:
    
    with open('mega_url.txt', 'r') as a:
        Link2 = a.read()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url=Link2)
except:
    pass

confirmtab()


mega = Mega()
try:
    m = mega.login(email_address, password)
    if m:
        print("Account Created successfully")
        print("Email : "+email_address+" \npass : "+password)
        with open('@Megapass.txt', 'a') as file:
            file.write(email_address+"\n")
            print("Email saved in @Megapass.txt !")
            upload_from_laptop("@Megapass.txt")
            print("Email Uploded")

except:
    pass

    