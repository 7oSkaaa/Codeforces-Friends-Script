import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from helpers.colors import colors

load_dotenv()

#Get the directory of current folder
directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory)


# scrapping the handles
def getHandles(file):
    f = open(file, "r")
    handles = f.read().strip().split('\n')
    return handles

# Create chrome driver
def createDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    return driver


# make timeout 30 seconds for command find element
def find_element(driver, by, value, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)), f'{colors.red}Timeout while trying to reach an element ❌{colors.reset}')


def addFriends(driver, Handles):
    
    # get handle and password from .env file
    Handle = os.getenv('CF_HANDLE')
    Password = os.getenv('CF_PASSWORD')
    removeExistFriends = os.getenv('REMOVE_EXIST_FRIENDS')
    
        
    # check if .env file is exist or not
    envExist = os.path.exists('.env')
    if not envExist:
        print(f'{colors.red}Please create .env file and add your Codeforces Handle and Password ❌{colors.reset}')
        return
    
    
    # check if handle and password is empty or not in .env file
    if not Handle or not Password or not removeExistFriends:
        print(f'{colors.red}Please set the environment variables ❌{colors.reset}')
        return


    # Login to Codeforces
    driver.get('https://codeforces.com/enter?back=%2F')
    find_element(driver, By.XPATH, '//*[@id="handleOrEmail"]').send_keys(Handle)
    find_element(driver, By.XPATH, '//*[@id="password"]').send_keys(Password)
    find_element(driver, By.XPATH, '//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input').click()
    print(f'{colors.blue}\nlogging in...{colors.reset}\n')
    time.sleep(5)
    
    
    # check if login is successful or not
    isLogged = False
    try:
        driver.find_element(By.XPATH, '//*[@id="enterForm"]/table/tbody/tr[3]/td[2]/div/span')
        isLogged = False
    except:
        isLogged = True
    
    
    if not isLogged:
        print(f'{colors.red}Login failed ... check your handle and password ❌\n{colors.reset}')
        driver.quit()
        return
    else:
        print(f'{colors.green}Login successful ✅{colors.reset}\n')
    
    
    # add friends
    for friendHandle in Handles:
        urlProfile = f'https://codeforces.com/profile/{friendHandle}'
        driver.get(urlProfile)
        time.sleep(2)
        
        # if no such handle exist
        currentUrl = driver.current_url
        if currentUrl == 'https://codeforces.com/':
            print(f'{colors.red}No such handle exist with {friendHandle} ❌{colors.reset}')
            continue
        
        
        # if handle is not a friend
        try:
            addFriend = driver.find_element(By.CLASS_NAME, 'addFriend')
            addFriend.click()
            print(f'{colors.gold}Added {friendHandle} as a friend ✅{colors.reset}')
        # if handle is already in friend list
        except NoSuchElementException:
            # option to remove friend
            if removeExistFriends == 'true':
                try:
                    removeFriend = driver.find_element(By.CLASS_NAME, 'removeFriend')
                    removeFriend.click()
                    print(f'{colors.beige}Removed {friendHandle} from friend list ✅{colors.reset}')
                except NoSuchElementException:
                    print(f'{colors.red}There is some error while removing {friendHandle} ⚠️{colors.reset}')
            # do nothing
            else:
                print(f'{colors.magenta}Already added {friendHandle} as a friend 🫰{colors.reset}')
        
        
def main():
    
    # get handles from Handles.txt
    Handles = getHandles('Handles.txt')
    
    # create driver
    driver = createDriver()
    
    # add friends to Codeforces
    addFriends(driver=driver, Handles=Handles)
    

if __name__ == "__main__":
    main()