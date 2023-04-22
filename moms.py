import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

idlist={
    '1':'lanikai0426',
    '2':'hae8477'
}
pwlist={
    '1':'wlgnsdl1',
    '2':'tkfkdhye1208'
}

for i in idlist:
    print(idlist[i])
    print(pwlist[i])
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    url='https://www.momsdiary.co.kr/member/out_login.html'
    driver.get(url)
    time.sleep(2)
    id=idlist[i]
    pw=pwlist[i]
    lid=driver.find_element(By.CSS_SELECTOR, '#out_con > div.out_left > div.out_left_b3 > form > div.out_login_b > div.out_login_id_f > input')
    lpw=driver.find_element(By.CSS_SELECTOR, '#out_con > div.out_left > div.out_left_b3 > form > div.out_login_b > div.out_login_pwd_f > input')
    lid.send_keys(id)
    time.sleep(1)
    lpw.send_keys(pw)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="out_con"]/div[1]/div[2]/form/div[4]/input').click()
    time.sleep(1)
    #글쓰기클릭
    # driver.find_element(By.XPATH, '//*[@id="contain"]/div[2]/div[1]/div[1]/a').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[1]/div[9]/a').click()
    # time.sleep(1)
    urls=f"https://mlog.momsdiary.co.kr/mydiary/diary/index.html?mlog_id={id}&mode=write"
    driver.get(urls)
    time.sleep(5)
    #driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[3]/table/tbody/tr[2]/td[2]/select/option[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/div[3]/table/tbody/tr[2]/td[2]/select/option[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="cm"]/div[3]/table/tbody/tr[5]/td[2]/input').send_keys('0')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="cm"]/div[3]/table/tbody/tr[10]/td/textarea').send_keys('0')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#cm > div.diary_write_box > table > tbody > tr:nth-child(14) > td.item_i3 > select > option:nth-child(1)').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="cm"]/div[3]/table/tfoot/tr[2]/td/input').click()
    time.sleep(2)
    driver.close()

driver.quit()