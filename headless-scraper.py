import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver 
import urllib.request
from time import sleep
import time
from datetime import datetime
import pandas as pd
#This one is intended to be run on a vps so there is no need for a normal selenium window
chrome_options = Options()
chrome_options.add_argument("--headless")
class Spring(object):
    def __init__(self, Spring):
        self.driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options) 
        self.Spring = Spring
    def login(self):
        count = 0
        try:
            self.driver.get('https://paws.gsu.edu/')
            li_btn = self.driver.find_element_by_xpath('//*[@id="ubtn-5757"]')
            li_btn.click()
            count+=1
            sleep(2)
            #here you want to enter your username and password
            id_in = self.driver.find_element_by_xpath('//*[@id="loginForm:username"]')
            id_in.send_keys('username')
            pass_in = self.driver.find_element_by_xpath('//*[@id="loginForm:password"]') 
            pass_in.send_keys('password')
            li_btn2 = self.driver.find_element_by_xpath('//*[@id="loginForm:loginButton"]')
            li_btn2.click()
            count+=1
            sleep(3)
            self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="contentDiv"]/div/div/div/div/strong/div/div[1]/iframe'))
            adddrop = self.driver.find_element_by_xpath('//*[@id="dashboard-info"]/div[1]/gsu-my-registration/div/button')
            adddrop.click()
            count+=1
            self.driver.switch_to_window(self.driver.window_handles[1])
            openn = self.driver.find_element_by_xpath('//*[@id="select2-chosen-1"]')
            openn.click()
            count+=1
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="202101"]').click()
            count+=1
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="term-go"]').click()
            count+=1
            sleep(2)
            class1 = self.Spring
            curr = '1'
            s = '"]'
            self.driver.find_element_by_xpath('//*[@id="enterCRNs-tab"]').click()
            count+=1
            tmp = '//*[@id="txt_crn' + curr + s
            self.driver.find_element_by_xpath(tmp).send_keys(class1)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="addCRNbutton"]').click()
            sleep(1)
            count+=1
            self.driver.find_element_by_xpath('//*[@id="saveButton"]').click()
            count+=1
            sleep(100)
            print("success")
            self.driver.quit()
        except:
            print("Spring except",count)
            sleep(2)
            self.driver.quit()
#getting the HTML from gosolar and saving that to the crn.txt
def getwebpage(url,crn):
    os.system("touch "+crn+".txt")
    urllib.request.urlretrieve(url, crn+".txt")
    file_path = crn+".txt"
    return file_path
#this basically checks if there is an open seat for the class by going to the line of the seatnumber for that class in the html
#so for each class you want you will need to find this if there are multiple classes on one page you will have to make sure it if the correct #
def check_open(file_path,line):
    with open(file_path) as f:
        text= f.readlines()
    
    seats_line = text[line]
    open_seats = seats_line[-7:-6]
    print(open_seats)
    if open_seats != '0':
        return True
    else:
        return False

def main(crns):
    
    start_time = time.time()
    #running the while loop for 25 days
    aday = 2160000
    while time.time() < start_time + aday:
        count += 1
        try:
            #This goes through each CRN after all CRN's have been ran it will loop again
            for index, row in crns.iterrows():
                crn = str(row['CRN'])
                url = row['URL']
                line = row['Line']
                r_cmd = "rm "+crn+".txt"
                os.system(r_cmd)
                file_path = getwebpage(url,crn)
                test = check_open(file_path,line)
                if test:
                    bot = Spring(crn)
                    bot.login()
        except Exception as e:
            #sometimes the html request will be rejected if that happens it will just wait for a bit and then start main again
            print(e)
            print("exception")
            sleep(15)
            main(crns)
            print("get html error")
        sleep(2)
crns = pd.read_csv("CRN.csv")
main(crns)



