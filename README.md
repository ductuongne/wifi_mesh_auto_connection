# WiFi Mesh Auto Login

Dự án tự động đăng nhập vào hệ thống WiFi Mesh công cộng.

## Mô tả

Script Python tự động đăng nhập vào hệ thống WiFi mesh mỗi giờ để duy trì kết nối internet. Hữu ích cho các mạng WiFi công cộng yêu cầu đăng nhập định kỳ.

## Yêu cầu hệ thống

- Python 3.6 trở lên
- Kết nối với mạng WiFi Mesh/Awing Connect

## Cài đặt

### Bước 1: Cài đặt Python

Tải và cài đặt Python từ [python.org](https://www.python.org/downloads/)

**Lưu ý:** Trong quá trình cài đặt, nhớ tick vào ô "Add Python to PATH"

### Bước 2: Clone hoặc tải dự án

```bash
git clone https://github.com/ductuongne/wifi_mesh_auto_connection
cd wifi_mesh_auto_connection
```

Hoặc tải file ZIP và giải nén.

### Bước 3: Cài đặt thư viện

Mở Command Prompt hoặc PowerShell trong thư mục dự án và chạy:

```bash
pip install -r requirements.txt
```

Lệnh này sẽ cài đặt các thư viện cần thiết:
- `requests` - Gửi HTTP requests
- `fake_useragent` - Tạo User-Agent ngẫu nhiên

## Cách chạy

### Cách 1: Chạy bằng file .bat (Windows)

Double-click vào file `run.bat`

### Cách 2: Chạy bằng Python

```bash
python wifi_mesh.py
```

### Cách 3: Chạy bằng PowerShell

```powershell
python wifi_mesh.py
```

## Hoạt động

Script sẽ:
1. Xóa màn hình console
2. Gửi yêu cầu đăng nhập đến server WiFi mesh
3. Kiểm tra và thông báo kết quả
4. Đợi 1 giờ (3600 giây)
5. Lặp lại từ bước 2

## Thoát chương trình

Nhấn `Ctrl + C` trong cửa sổ console để dừng script.

## Xử lý sự cố

### Lỗi: `ModuleNotFoundError`

Chạy lại lệnh cài đặt thư viện:
```bash
pip install -r requirements.txt
```

### Lỗi: Không kết nối được

- Kiểm tra kết nối WiFi
- Đảm bảo bạn đã kết nối với mạng WiFi Mesh/Awing Connect
- Kiểm tra tên đăng nhập và mật khẩu

### Script không tự động đăng nhập lại

- Kiểm tra xem script có còn đang chạy không
- Xem log trong console để biết chi tiết lỗi

## Cấu trúc dự án

```
wifi/
│
├── wifi_mesh.py      # Script chính
├── requirements.txt   # Danh sách thư viện
├── run.bat           # File chạy nhanh (Windows)
└── README.md         
```

## Lưu ý

- Script cần chạy liên tục để duy trì đăng nhập tự động
- Thời gian đăng nhập lại mặc định là 1 giờ, có thể thay đổi trong code (`time.sleep(3600)`)
- Không chia sẻ thông tin đăng nhập của bạn


