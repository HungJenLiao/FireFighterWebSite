from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from fake_useragent import UserAgent
import time, random
import pandas as pd
import numpy as np

def data_cleaning(df):
    #處理缺失值
    df.fillna("0", inplace = True)
    #處理時間格式
    df_time = df["案發日期"]
    df_time_num = df_time.count()
    context = []

    for index, single_time in enumerate(df_time):
        if single_time == "0":
            single_time = '9999/12/31 12:12:12'
        single_time = single_time.replace("/", "-")
        context.append(single_time)
    df["案發日期"] = context

    #處理locations
    df_locations = df["發生地點"]
    df_locations_num = df_locations.count()
    df_status = df["狀態"]
    
    return df_locations, df_locations_num, df_status

def search_addr(address):
    #設定ChromeDriver的執行路徑
    options = Options()
    options.chrome_executable_path = "./chromedriver"
    #設定user-agent
    user_agent = UserAgent().random
    print(user_agent)
    options.add_argument("user-agent={}".format(user_agent))
    #不開啟視窗
    options.add_argument("--headless")
    #使用無痕留覽器
    # options.add_argument("--incognito")
    #proxy
    proxy = "190.61.88.147:8080"
    options.add_argument(f'--proxy-server={proxy}')
    #建立Driver實體物件，用程式操作瀏覽器
    driver = webdriver.Chrome(options = options)

    try:
        #連線到 台灣地圖服務網
        target_url = "https://www.map.com.tw/"
        driver.get(target_url)

        rest= random.randint(3,5)
        time.sleep(rest)

        #自動化搜尋
        addr = address
        search = driver.find_element(By.ID, "searchWord") #找到網頁上id 相等的元素
        search.clear()
        search.send_keys(addr)
        driver.find_element(By.XPATH, "/html/body/form/div[10]/div[2]/img[2]").click()

        time.sleep(rest)

        #跳轉頁面
        iframe = driver.find_element(By.CLASS_NAME, "winfoIframe")  
        driver.switch_to.frame(iframe)  
        #截取所需資料
        info = driver.find_element(By.XPATH, "/html/body/form/div[4]/table/tbody/tr[1]/td/table/tbody/tr[4]/td")
        time.sleep(5)
        info_result = info.text
        driver.close()
        status = 1
        return info_result, status
    except NoSuchElementException:
        time.sleep(2)
        print("No such element")
        driver.close()
        status = 0
        return "Error!!! " + address, status

def write_to_file(FileName, df_name):
    file_name = FileName
    writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
    df_name.to_excel(writer, index = False)
    writer.save()
    print('Successfully exported into Excel File')

##################################
#local test
##################################
#import excel檔案
# df = pd.read_excel("埔里12月救護紀錄拷貝.xlsx")
# df = df.head(2)
# df = df[['案發日期', '出勤車輛', '案件細項', '發生地點']]
# status_value = np.zeros(len(df.index), dtype = np.int)
# # # print(status_value.size)
# df.insert(len(df.columns), '狀態', status_value)
# # #處理缺失值
# df.fillna("0", inplace = True)
# # # print(df)

# df_info = data_cleaning(df)
# # print(df_info[2])
# # print(df_info[0].iloc[119])
# df_locations = df_info[0]
# # df_locations_num = df_info[1]
# df_locations_num = 2
# df_status = df_info[2]
# for num in range(0, df_locations_num):
#     info_result = search_addr(df_locations[num])
#     df_locations[num] = info_result[0]
#     df_status[num] = info_result[1]
#     print(df_locations[num])
# df["發生地點"] = df_locations



# print('Location Transform Successfully!!')
# print("轉換成功")
# write_to_file("NewLocation.xlsx", df)
#########################################




    
