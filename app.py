from flask import Flask, render_template, request, jsonify
import os
import datetime
import json

app = Flask(__name__)

# 用於存儲用戶輸入的數據
user_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        name = data.get('name', '')
        message = data.get('message', '')
        
        if not name or not message:
            return jsonify({'success': False, 'error': '請填寫所有欄位'}), 400
        
        # 添加時間戳
        entry = {
            'name': name,
            'message': message,
            'timestamp': datetime.datetime.now().isoformat(),
            'id': len(user_data) + 1
        }
        
        user_data.append(entry)
        
        return jsonify({
            'success': True, 
            'message': '數據提交成功！',
            'data': entry
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data')
def get_data():
    return jsonify({
        'success': True,
        'data': user_data,
        'count': len(user_data)
    })

@app.route('/api/clear', methods=['POST'])
def clear_data():
    global user_data
    user_data = []
    return jsonify({'success': True, 'message': '所有數據已清除'})

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'data_count': len(user_data)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
