import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import settings as set
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  
from selenium.webdriver.chrome.options import Options
import json 

def get_selenium(url, date_list):
    result = []

    chrome_options = Options()
    chrome_options.headless = True # headless 설정
    # enable browser logging
    d = DesiredCapabilities.CHROME.copy()
    d['loggingPrefs'] = { 'performance':'ALL' }
    d['goog:loggingPrefs'] = {'performance': 'ALL'}

    
    try:
        driver = webdriver.Chrome(executable_path='chromedriver', desired_capabilities=d)
        element = WebDriverWait(driver, 5).until(   
            EC.presence_of_element_located((By.TAG_NAME, 'body'))) # body 태그를 찾을 때까지 5초 대기

        for i in date_list:

            if int(i[8:]) == 1 :
                print(i[5:7] + "월 시작..")
            url_1 = url + i ### 텍스트 누적되어 나오는게 url에 겹겹이 i를 쌓아서 그러는 것 같음
            driver.get(url=url_1)
            performance_log = driver.get_log('performance') # driver.get_log(log_type)
            
            status = get_status(performance_log)
            text = (driver.find_element(By.XPATH, '/html/body')).text
            result.append((text, status))
        result = tuple(result)
        return result
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def get_status(logs):
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            try:
                response_received = d['message']['method'] == 'Network.responseReceivedExtraInfo'
                status_code = d['message']['params']['statusCode']
                if status_code and response_received:
                    return d['message']['params']['statusCode']
            except:
                pass
