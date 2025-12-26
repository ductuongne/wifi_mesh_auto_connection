import requests
import time
import os
from fake_useragent import UserAgent

def login_wifi(username, password):

    ua = UserAgent().random
    
    url1 = "http://186.186.0.1/login"
    url2 = "http://free.wi-mesh.vn/login"
    payload = {
        "username": username,
        "password": password,
        "dst": "http://v1.awingconnect.vn/Success",
        "popup": "false"
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "186.186.0.1",
        "Origin": "http://v1.awingconnect.vn",
        "Referer": "http://v1.awingconnect.vn/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua,
    }
    try:
        response = requests.post(url1, data=payload, headers=headers)
    except:
        response = requests.post(url2, data=payload, headers=headers)

    if response.status_code == 200:
        print("✅ Đã gửi yêu cầu đăng nhập.")
        if "Success" in response.text or "Internet" in response.text:
            print("✅ Đăng nhập thành công.")
        else:
            print("❌ Có thể đăng nhập không thành công.")
    else:
        print(f"❌ Lỗi khi gửi request: {response.status_code}")


os.system("cls")
while True:

    login_wifi("awing60", "Awing60@2018")
    # chờ 60p thì gửi request lại
    time.sleep(3600)
    

# awing60
# Awing60@2018