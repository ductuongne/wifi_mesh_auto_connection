import requests
import time
import os
from fake_useragent import UserAgent

logo = """ 
\033[1;36m                     ██░ ██  ▄▄▄       ▄████▄   ██░ ██  ██▓ ███▄ ▄███▓ ▄▄▄       ███▄    █ 
                    ▓██░ ██▒▒████▄    ▒██▀ ▀█  ▓██░ ██▒▓██▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
                    ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▒██▀▀██░▒██▒▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
\033[1;93m                    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░▓█ ░██ ░██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
                    ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░░▓█▒░██▓░██░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
                    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░ ▒ ░░▒░▒░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
                    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒    ▒ ░▒░ ░ ▒ ░░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
                    ░  ░░ ░  ░   ▒   ░         ░  ░░ ░ ▒ ░░      ░     ░   ▒      ░   ░ ░ 
                    ░  ░  ░      ░  ░░ ░       ░  ░  ░ ░         ░         ░  ░         ░ 
                                    ░                                                              
                                    TOOL TỰ ĐỘNG KẾT NỐI LẠI WIFI MESH BY @ductuongug                   
"""

def logout_wifi():

    url1 = "http://186.186.0.1/logout?"
    url2 = "http://free.wi-mesh.vn/logout?"

    try:
        response = requests.get(url1)
    except:
        response = requests.get(url2)


def login_wifi(username, password):

    ua = UserAgent().chrome
    
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
    
    # Thử đăng nhập với URL1
    try:
        print("🔄 Đang thử đăng nhập qua URL1...")
        response = requests.post(url1, data=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            if "Success" in response.text or "Internet" in response.text:
                print("✅ Đăng nhập thành công qua URL1.")
                return True
            else:
                print("⚠️ URL1 phản hồi nhưng đăng nhập không thành công, thử URL2...")
        else:
            print(f"⚠️ URL1 trả về status code {response.status_code}, thử URL2...")
            
    except Exception as e:
        print(f"⚠️ Không thể kết nối URL1: {str(e)}, thử URL2...")
    
    # Nếu URL1 thất bại, thử URL2
    try:
        print("🔄 Đang thử đăng nhập qua URL2...")
        response = requests.post(url2, data=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            if "Success" in response.text or "Internet" in response.text:
                print("✅ Đăng nhập thành công qua URL2.")
                return True
            else:
                print("❌ URL2 phản hồi nhưng đăng nhập không thành công.")
                return False
        else:
            print(f"❌ URL2 trả về status code {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Không thể kết nối URL2: {str(e)}")
        return False


def main():
    os.system("cls")
    print(logo)
    while True:
        logout_wifi()
        login_wifi("awing60", "Awing60@2018")
        # chờ 60p thì gửi request lại
        time.sleep(3600)

if __name__ == "__main__":
    main()

# awing60
# Awing60@2018