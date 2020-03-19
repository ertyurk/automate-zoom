from selenium import webdriver
from time import sleep
from details import contentType, contentDir, zoomEmail, zoomPass

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", contentDir)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", contentType)



class run():
    def __init__(self):
        self.driver = webdriver.Firefox(firefox_profile=profile) 
        
    def login(self):
        self.driver.get('https://zoom.us/signin')
        sleep(2)

        email_in = self.driver.find_element_by_id('email')
        email_in.send_keys(zoomEmail)
        sleep(0.5)

        pw_in = self.driver.find_element_by_id('password')
        pw_in.send_keys(zoomPass)
        sleep(0.5)

        login_btn = self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/div/div[1]/a')
        login_btn.click()       
        sleep(1)
        
    def recordings(self):
        self.driver.get('https://zoom.us/recording')     
        sleep(2)
        
        findFile = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div[5]/div[1]/a')
        findFile.click()
        
        downFile = self.driver.find_element_by_xpath('//*[@id="recording-list-thumbnail"]/div/div/div[1]/div[2]/a[1]')
        downFile.click()
        sleep(2)
        quit()
        
bot = run()
bot.login()
bot.recordings()
