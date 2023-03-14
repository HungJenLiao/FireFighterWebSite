# Django Project - FireFighterWebSite
#### 這個網頁是利用Selenium自動化爬蟲將資料庫中的地址丟進台灣地圖服務網進行正確地址的轉換，並且抓取下來存進資料庫。在網頁在可以使用基本表單的操作CRUD(Creat-Read-Update-Delete)，並將資料結果視覺化
資料庫：使用內建的sqlite. 

前端：使用Boostrap結合Template. 

後端：使用Django Model Form 快速開發CRUD的功能. 

***
### 功能一 登入、登出頁面
Login
```python
def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/dashboard/')
    else:
        return render(request, 'login.html')
```
Logout
```python
def logout(request):
    auth.logout(request)
    return redirect('/accounts/login/')
```
### 功能二 上傳Excel並匯入資料庫
UploadFile
```python
@login_required
def uploadFile(request):
    #get user name
    fullname = request.user.get_full_name()

    if request.method == 'POST':
        #創建資料夾
        uploadDir = BASE_DIR + '/upload'
        if not isdir(uploadDir):
            mkdir(uploadDir)
        print(uploadDir)
        #抓取上傳資料
        uploadedFile = request.FILES.get('uploadFile')
        if not uploadedFile:
            return render(request, 'uploadFile.html', {'msg': '沒有選擇文件'})
        if not uploadedFile.name.endswith('.xlsx'):
            return render(request, 'uploadFile.html', {'msg': '必須選擇xlsx文件'})
        #資料轉換的Functioin
        nameTransform(uploadedFile)
        return render(request, 'uploadFile.html', {'fullname': fullname})
    return render(request, 'uploadFile.html', {'fullname': fullname})
```
### 功能三 使用Selenium爬蟲抓取所需資料
```python
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
    #使用其他proxy
    proxy = "XXX.XX.XX.XXX:XXXX"
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
```
### 功能四 使用Django Model Form建立CRUD
#### Read
```python
@login_required
def emergency_list(request):
    #Login FullName
    fullname = request.user.get_full_name()
    #Get Emergency List Inofrmation
    emergency_list = Emergency.objects.all().order_by("id")
    context = {'fullname': fullname, 'emergency_list': emergency_list}
    return render(request, 'emergency_list.html', context)
```
#### Edit
```python
@login_required
def emergency_list_edit(request):
    #Login FullName
    fullname = request.user.get_full_name()
    #Form
    submitted = False
    if request.method == "POST":
        form = EmergencyForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'fullname': fullname, 'form': form}
            return HttpResponseRedirect('/emergency_list/edit?submitted=True/', context)
    else:
        form = EmergencyForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'fullname': fullname, 'form': form, 'submitted': submitted}
    return render(request, 'emergency_list_edit.html', context)
```
#### Update
```python
@login_required
def emergency_list_update(request, Em_id):
    #Login FullName
    fullname = request.user.get_full_name()
    #Get Each ID
    emergency_obj = Emergency.objects.get(pk = Em_id)
    #Form request or None
    form = EmergencyForm(request.POST or None, instance = emergency_obj)
    if form.is_valid():
        form.save()
        return redirect('EmList')
    context = {'fullname': fullname, 'emergency_obj': emergency_obj, 'form': form}
    return render(request, 'emergency_list_update.html', context)
```
#### Delete
```python 
@login_required
def emergency_list_delete(request, Em_id):
    #Get Each ID
    emergency_obj = Emergency.objects.get(pk = Em_id)
    #Delete
    emergency_obj.delete()
    return redirect('EmList')
```
