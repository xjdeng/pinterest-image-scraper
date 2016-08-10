from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time,random,socket,unicodedata
import string, copy
import pandas as pd

def randdelay(a,b):
    time.sleep(random.uniform(a,b))

def u_to_s(uni):
    return unicodedata.normalize('NFKD',uni).encode('ascii','ignore')

class Pinterest_Helper(object):
    
    def __init__(self, login, pw):
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.pinterest.com")
        # emailElem = self.browser.find_element_by_id('userEmail')
        emailElem = self.browser.find_element_by_name('email')
        emailElem.send_keys(login)
        # passwordElem = self.browser.find_element_by_id('userPassword')
        passwordElem = self.browser.find_element_by_name('password')
        passwordElem.send_keys(pw)
        passwordElem.send_keys(Keys.RETURN)
        randdelay(2,4)
    
    def getURLs(self, urlcsv, threshold = 500):
        tmp = self.read(urlcsv)
        results = []
        for t in tmp:
            tmp3 = self.runme(t, threshold)
            results = list(set(results + tmp3))
        random.shuffle(results)
        return results
    
    def write(self, myfile, mylist):
        tmp = pd.DataFrame(mylist)
        tmp.to_csv(myfile, index=False, header=False)
    
    def read(self,myfile):
        tmp = pd.read_csv(myfile,header=None).values.tolist()
        tmp2 = []
        for i in range(0,len(tmp)):
            tmp2.append(tmp[i][0])
        return tmp2        
        
    
    def runme(self,url, threshold = 500):
        final_results = []
        previmages = []
        tries = 0
        try:
            self.browser.get(url)
            while threshold > 0:
                try:
                    results = []
                    images = self.browser.find_elements_by_tag_name("img")
                    if images == previmages:
                        tries += 1
                    else:
                        tries = 0
                    if tries > 20:
                        return final_results
                    for i in images:
                        src = i.get_attribute("src")
                        if src:
                            if string.find(src,"/236x/") != -1:
                                src = string.replace(src,"/236x/","/736x/")
                                results.append(u_to_s(src))
                    previmages = copy.copy(images)
                    final_results = list(set(final_results + results))
                    dummy = self.browser.find_element_by_tag_name('a')
                    dummy.send_keys(Keys.PAGE_DOWN)
                    # images[0].send_keys(Keys.PAGE_DOWN)
                    randdelay(0,1)
                    threshold -= 1
                except (StaleElementReferenceException):
                    threshold -= 1
        except (socket.error, socket.timeout):
            pass
        return final_results
        
 
    def scrape_old(self, url):
        results = []
        self.browser.get(url)
        images = self.browser.find_elements_by_tag_name("img")
        for i in images:
            src = i.get_attribute("src")
            if src:
                if string.find(src,"/236x/") != -1:
                    src = string.replace(src,"/236x/","/736x/")
                    results.append(u_to_s(src))
        return results
            
        
        
        
        
    
    def close(self):
        self.browser.close()
    
    
    