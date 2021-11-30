# PyQT使用

## 安裝

1. PyCharm
2. pip install pyqt5-tools 
3. QtDesigner

## PyCharm設定
1. 打開PyCharm左上角 file > Settings
2. Settings > Tools > External Tools
3. 新增並編輯一個Tool
- Name : 都可以
- Tool Settings
- Program 選取pyuic5.exe
- Arguments : $FileName$ -o $FileNameWithoutExtension$.py
- Working directory: $FileDir$

## 轉檔
1. 在PyCharm底下對著 ui檔案 右鍵選 External Tools > 剛剛建立的Tools
2. 即可成功轉檔

## git 帳號密碼自動存檔
```sh
git config --global credential.helper store
```



