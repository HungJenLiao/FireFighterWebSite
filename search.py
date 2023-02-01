from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent
import time, random
import pandas as pd

def sumup(a, b):
    sum = a + b
    return sum

def search_addr(address):
    #設定ChromeDriver的執行路徑
    options = Options()
    options.chrome_executable_path = "./chromedriver"
    #設定user-agent
    options.add_argument("user-agent={Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36}")
    #不開啟視窗
    options.add_argument("--headless")
    #建立Driver實體物件，用程式操作瀏覽器
    driver = webdriver.Chrome(options = options)

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
    # time.sleep(5)
    info_result = info.text
    driver.close()
    return info_result

def write_to_file(FileName, df_name):
    file_name = FileName
    writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
    df_name.to_excel(writer, index = False)
    writer.save()
    print('Successfully exported into Excel File')

# #import excel檔案
# df = pd.read_excel("test.xlsx")
# #新增id
# # df.reset_index(inplace = True)
# # df.rename(columns = {'index':'id'}, inplace = True)
# #處理時間格式
# df_time = df["案發日期"]
# df_time_num = df_time.count()

# for num in range(0, df_time_num):
#     df_time[num] = df_time[num].replace("/", "-")
# df_time = df["案發日期"]
# #處理locations
# df_locations = df["發生地點"].head(2)
# df_locations_num = df_locations.count()

# for num in range(0, df_locations_num):
#     df_locations[num] = search_addr(df_locations[num])
#     print(num)
# df_locations = df["發生地點"]

# print('Location Transform Successfully!!')
# write_to_file("NewLocation.xlsx", df)




    
