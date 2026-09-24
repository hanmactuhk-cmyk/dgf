# Hn38videoAItool

Công cụ desktop Windows mô phỏng **workflow của bản ZIP gốc** theo cấu trúc dễ build bằng GitHub Actions:

- Giao diện desktop tiếng Việt.
- Tạo job video từ prompt.
- Chọn thời lượng và tỉ lệ khung hình.
- Hàng đợi nhiều job.
- Theo dõi trạng thái: chờ → đang xử lý → hoàn tất / lỗi / đã huỷ.
- Tự động polling backend.
- Tải MP4 về máy.
- Retry / Cancel.
- Lịch sử job.
- Có local bridge API để extension hoặc ứng dụng khác gọi vào.
- Có Chrome Extension shell đặt trong `assets/extension`.
- Build `.exe` bằng `Hn38videoAItool.spec`.

## Lưu ý

Bản này bám theo **kiến trúc và workflow** của ZIP gốc nhưng không sao chép hoặc triển khai các cơ chế lấy cookie/session/token, giả mạo CAPTCHA hoặc vượt cơ chế bảo mật.

Phần backend được tách thành adapter (`desktop/services/backend.py`). Bạn có thể nối nó với **API chính thức hoặc endpoint mà bạn được phép sử dụng**.

## Chạy bằng Python

```bat
pip install -r requirements
python desktop\main.py
```

## Build EXE

```bat
pip install -r requirements
pip install pyinstaller
pyinstaller --noconfirm --clean Hn38videoAItool.spec
```

File build nằm trong `dist/`.

## GitHub Actions

Push project lên GitHub rồi chạy:

**Actions → HN38 Video AI Tool → Run workflow**

Artifact `Hn38videoAItool-Windows` sẽ chứa bản build Windows.

## Cấu hình backend

Ứng dụng mặc định chạy chế độ demo để có thể kiểm tra toàn bộ giao diện và queue.

Cấu hình API nằm trong:

`%APPDATA%\Hn38videoAItool\config.json`

Không commit API key/token vào GitHub.

Nếu backend của bạn trả JSON theo dạng tương tự:

```json
{
  "id": "job_123",
  "status": "processing",
  "progress": 45
}
```

và khi hoàn tất:

```json
{
  "id": "job_123",
  "status": "completed",
  "video_url": "https://example.com/video.mp4"
}
```

thì có thể dùng adapter có sẵn hoặc chỉnh `desktop/services/backend.py`.

## Cấu trúc

```text
Hn38videoAItool/
├── .github/
│   └── workflows/
│       └── main.yml
├── assets/
│   └── extension/
├── data/
├── desktop/
│   ├── main.py
│   ├── services/
│   │   ├── backend.py
│   │   └── job_manager.py
│   └── ui/
│       └── app.py
├── .gitignore
├── Hn38videoAItool.spec
├── README.md
└── requirements
```
