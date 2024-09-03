import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriverのパス
chrome_driver_path = '/opt/homebrew/bin/chromedriver'  # 必要に応じてパスを調整

# Chromeオプションの設定
chrome_options = Options()
#chrome_options.add_argument("--headless")  # ヘッドレスモードで実行する場合
chrome_options.add_argument("--disable-gpu")

# ログイン情報を取得
login_info_path = 'login_info.txt'
with open(login_info_path, 'r') as file:
    lines = file.readlines()
    email = lines[0].split('=')[1].strip()
    password = lines[1].split('=')[1].strip()

# WebDriverの初期化
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Discordにアクセス
driver.get('https://discord.com/login')

# ログインページがロードされるまで待機
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]')))

# ログイン情報を入力
email_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'password')
email_input.send_keys(email)  # ファイルから取得したメールアドレスを入力
password_input.send_keys(password)  # ファイルから取得したパスワードを入力

# ログインボタンをクリック
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

# ログイン待機
time.sleep(20)  # ログイン処理に応じて調整してください

# 特定のチャンネルに移動
channel_url = 'https://discord.com/channels/973157270554804264/973162050333327390'
driver.get(channel_url)

# メッセージがロードされるまで待機
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="message"]')))

# 最新メッセージを取得
messages = driver.find_elements(By.CSS_SELECTOR, 'div[class*="messageContent"]')

if messages:
    latest_message = messages[-1].text  # 最後のメッセージが最新
    print(f'最新メッセージ: {latest_message}')

    # ギフトコードを抽出
    match = re.search(r'Code:\s*(\w+)', latest_message)
    if match:
        gift_code = match.group(1)
        print(f'ギフトコード: {gift_code}')
        
        # giftcode.txtに保存
        with open('giftcode.txt', 'w') as file:
            file.write(gift_code)
    else:
        print("ギフトコードが見つかりませんでした。")
else:
    print("メッセージが見つかりませんでした。")

# ブラウザを閉じる
driver.quit()
