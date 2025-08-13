# 🚀 Render部署測試應用程式

這是一個簡單的互動型Python Flask應用程式，專門用於測試GitHub到Render的部署流程。

## 功能特色

- ✅ 現代化的響應式UI設計
- ✅ 互動式表單提交
- ✅ 即時數據顯示
- ✅ 健康檢查端點
- ✅ 完整的錯誤處理
- ✅ 載入動畫效果

## 本地開發

### 前置需求

- Python 3.7+
- pip

### 安裝步驟

1. 克隆專案：
```bash
git clone <your-repo-url>
cd render-deployment-test
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 運行應用程式：
```bash
# 開發環境
python app.py

# 或使用啟動腳本
start.bat
```

4. 開啟瀏覽器訪問：`http://localhost:5000`

## 部署到Render

### 方法一：透過GitHub自動部署

1. **準備GitHub倉庫**
   - 將此專案推送到GitHub
   - 確保包含以下文件：
     - `app.py` (主應用程式)
     - `requirements.txt` (Python依賴)
     - `templates/index.html` (前端模板)

2. **在Render創建新服務**
   - 登入 [Render](https://render.com)
   - 點擊 "New +" → "Web Service"
   - 連接您的GitHub帳戶
   - 選擇此專案倉庫

3. **配置服務設定**
   - **Name**: `render-deployment-test` (或您喜歡的名稱)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: 選擇免費方案

4. **環境變數設定** (可選)
   - `ENVIRONMENT`: `production`

5. **點擊 "Create Web Service"**

### 方法二：手動部署

如果您想手動部署，可以：

1. 在Render創建新的Web Service
2. 選擇 "Deploy from existing code"
3. 上傳專案文件

## 測試部署

部署完成後，您可以：

1. **基本功能測試**
   - 訪問應用程式首頁
   - 提交表單數據
   - 查看數據列表
   - 清除數據

2. **API端點測試**
   - `GET /` - 首頁
   - `POST /api/submit` - 提交數據
   - `GET /api/data` - 獲取數據
   - `POST /api/clear` - 清除數據
   - `GET /health` - 健康檢查

3. **健康檢查**
   - 訪問 `/health` 端點
   - 檢查應用程式狀態

## 故障排除

### 常見問題

1. **部署失敗**
   - 檢查 `requirements.txt` 是否正確
   - 確認 `app.py` 中的端口設定
   - 查看Render的部署日誌

2. **應用程式無法啟動**
   - 確認Start Command正確
   - 檢查環境變數設定
   - 查看應用程式日誌

3. **靜態文件問題**
   - 確認 `templates` 目錄結構正確
   - 檢查HTML文件路徑

### 日誌查看

在Render控制台中：
1. 點擊您的服務
2. 進入 "Logs" 標籤
3. 查看實時日誌

## 專案結構

```
render-deployment-test/
├── app.py                 # 主應用程式
├── requirements.txt       # Python依賴
├── README.md             # 說明文件
└── templates/
    └── index.html        # 前端模板
```

## 技術棧

- **後端**: Python Flask
- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **部署**: Render
- **版本控制**: Git/GitHub

## 授權

此專案僅用於測試目的，可自由使用和修改。

---

**提示**: 這個應用程式使用記憶體存儲數據，重新部署後數據會重置。在生產環境中，建議使用資料庫來持久化數據。
