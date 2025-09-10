# 在相同路徑可直接載入自己建的py檔
import model
import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# 創建了一個 Flask 應用實例，__name__ 參數告訴 Flask 使用當前模塊的名稱來配置應用

CORS(app)
# 將 CORS 配置應用到你的 Flask 應用，使其可以處理來自不同來源的請求

@app.route('/')
# 作用是定義當用戶訪問特定路徑時，應該由哪個函數來處理請求和生成響應
# '/' 指的是根路徑

# 當用戶訪問根 URL（/）時執行下面的函數
def index():
    return '媽我肚子餓了'


# 當用戶發送 POST 請求到 /predict 路徑時，這個函數將被調用
# 下列需用postman才可運行
@app.route('/predict', methods=['POST'])
def postInput():
    try:
        # 獲取來自客戶端的 JSON 數據
        insertValues = request.get_json()

        # 驗證請求中是否包含所有必需的鍵
        if not all(key in insertValues for key in ['sepalLengthCm', 'sepalWidthCm', 'petalLengthCm', 'petalWidthCm']):
            return jsonify({'error': 'Invalid input'}), 400

        # 提取數據並轉換為數字
        x1 = insertValues['sepalLengthCm']
        x2 = insertValues['sepalWidthCm']
        x3 = insertValues['petalLengthCm']
        x4 = insertValues['petalWidthCm']
        input = np.array([[float(x1), float(x2), float(x3), float(x4)]])

        # 使用模型進行預測
        result = model.predict(input)

        # 返回預測結果
        return jsonify({'return': str(result[0])})

    except Exception as e:
        # 返回錯誤信息
        return jsonify({'error': str(e)}), 500
    # jsonify 將預測結果包裝成 JSON 格式的響應，並返回給前端


# 這行代碼的意思是當這個腳本被直接執行時，下面的代碼塊將會被運行。如果這個腳本被作為模塊導入到其他腳本中，這段代碼將不會被執行
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    # app.run() 是 Flask 應用實例的方法，用於啟動應用服務器
    # host='0.0.0.0' 允所有 IP 位址連接
    # port=3000 設置伺服器的埠號
    # debug=True 開啟除錯模式，當程式出錯時可以顯示錯誤訊息