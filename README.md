# Tetris_program-exe

已打包為獨立 Windows 可執行檔 `Tetris.exe`（為本 repo 之主要專題檔案），無需安裝 Python 或第三方套件即可直接執行。



## 簡介
`Tetris_program-exe` 為作者課餘自主製作的俄羅斯方塊（Tetris）專題作品。專案重點放在遊戲機制、方塊旋轉/碰撞處理與遊戲流程設計；主程式已打包成可執行檔，方便評審或教授快速執行與體驗。
Repo 內亦保留若干個人 Python 練習檔（例如：principal,practice,api），僅為學習用途，**與主專題功能無關**。



## 主要功能
- 單人模式：分數、等級、速度遞增。
- 雙人同機對戰（本機）：鍵盤分區對戰，含基本攻擊機制。
- 方塊旋轉與碰撞處理：以 4x4 模板矩陣表示方塊，採矩陣旋轉並做邊界/格子碰撞檢查，包含簡易 wall-kick 行為。
- 高分儲存：將高分寫入本地檔案（JSON 格式）。



## 如何開始遊戲
1. 下載本 repo。
2. 在根目錄找到 `Tetris_program-exe`。
3. 直接雙擊 `Tetris.exe` 即可啟動遊戲。



## 操作說明（預設鍵位）
BackSpace：退回到前一個頁面

Enter：前進到下一個頁面

左 / 右：移動方塊

上：旋轉方塊

下：加速落下

空白：立即落下

Lctrl：儲存方塊



## 開發重點（技術摘要）

方塊表示：使用格子 (grid) 與 4x4 方塊模板表示不同方塊型態。

旋轉邏輯：以矩陣旋轉結合邊界與格子碰撞檢查；遇到碰撞時嘗試左右偏移（簡易 wall-kick），若仍不可行則回滾旋轉。

消行處理：由底層往上掃描滿行並刪除，同時更新分數與等級，等級提升會提高下落速度。

高分儲存：以 JSON 檔存放於執行目錄，便於讀取與展示。



## 遊戲節圖

![screenshot1](screenshot/screenshot1.png)
![screenshot2](screenshot/screenshot2.png)
![screenshot3](screenshot/screenshot3.png)
![screenshot4](screenshot/screenshot4.png)
![screenshot5](screenshot/screenshot5.png)
![screenshot6](screenshot/screenshot6.png)

