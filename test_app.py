#!/usr/bin/env python3
"""
簡單的應用程式測試腳本
用於驗證Flask應用程式是否正常工作
"""

import requests
import json
import time
import sys

def test_app():
    """測試應用程式的基本功能"""
    base_url = "http://localhost:5000"
    
    print("🚀 開始測試Render部署測試應用程式...")
    print("=" * 50)
    
    # 測試1: 健康檢查
    print("1. 測試健康檢查端點...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ 健康檢查成功: {data['status']}")
            print(f"   📊 數據數量: {data['data_count']}")
        else:
            print(f"   ❌ 健康檢查失敗: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ 無法連接到應用程式: {e}")
        return False
    
    # 測試2: 獲取初始數據
    print("\n2. 測試獲取數據端點...")
    try:
        response = requests.get(f"{base_url}/api/data", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ 獲取數據成功: {data['count']} 條記錄")
        else:
            print(f"   ❌ 獲取數據失敗: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ 無法獲取數據: {e}")
        return False
    
    # 測試3: 提交測試數據
    print("\n3. 測試提交數據...")
    test_data = {
        "name": "測試用戶",
        "message": "這是一條測試訊息，用於驗證部署是否成功！"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/submit",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ 提交數據成功: {data['message']}")
        else:
            print(f"   ❌ 提交數據失敗: {response.status_code}")
            print(f"   回應: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ 無法提交數據: {e}")
        return False
    
    # 測試4: 再次獲取數據確認
    print("\n4. 確認數據已保存...")
    try:
        response = requests.get(f"{base_url}/api/data", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ 數據已保存: {data['count']} 條記錄")
            if data['count'] > 0:
                latest = data['data'][-1]
                print(f"   📝 最新記錄: {latest['name']} - {latest['message']}")
        else:
            print(f"   ❌ 獲取數據失敗: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ 無法獲取數據: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 所有測試完成！應用程式運行正常。")
    print("\n📋 下一步:")
    print("1. 將此專案推送到GitHub")
    print("2. 在Render創建新的Web Service")
    print("3. 連接GitHub倉庫進行自動部署")
    print("4. 等待部署完成後測試線上版本")
    
    return True

if __name__ == "__main__":
    print("請確保應用程式正在運行 (python app.py)")
    print("然後在另一個終端中運行此測試腳本")
    print()
    
    try:
        success = test_app()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n測試被中斷")
        sys.exit(1)
