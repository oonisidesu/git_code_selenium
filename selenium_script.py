from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriverのパス
chrome_driver_path = '/opt/homebrew/bin/chromedriver'  # chromedriverのパスに置き換えてください

# id.txtからIDを読み込みます
with open('id.txt', 'r') as id_file:
    ids = id_file.readlines()

# gitcode.txtからギフトコードを1つ読み込みます
with open('gitcode.txt', 'r') as code_file:
    gift_code = code_file.readline().strip()

# IDのリストから改行を取り除きます
ids = [id.strip() for id in ids]

# Chromeオプションの設定
chrome_options = Options()
#chrome_options.add_argument("--headless")  # ヘッドレスモードで実行する場合

# WebDriverの初期化
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 目的のURLを開きます
driver.get('https://wos-giftcode.centurygame.com/')

# 各IDに対してループ処理を行います
for player_id in ids:
    try:
        # 前回のセッションが残っている場合、「終了」ボタンをクリックしてリセットします
        try:
            exit_button = driver.find_element(By.CSS_SELECTOR, 'div.exit_con')
            exit_button.click()
            time.sleep(1)  # ボタン押下後の処理時間を待つ
            print(f'ID: {player_id} の前のセッションをリセットしました。')
        except:
            print(f'ID: {player_id} の前のセッションはリセット不要でした。')

        # プレイヤーIDの入力フィールドを見つけ、IDを入力します
        id_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="プレイヤーID"]')
        id_input.clear()
        id_input.send_keys(player_id)

        # 「ログイン」ボタンをクリックします
        login_button = driver.find_element(By.CSS_SELECTOR, 'div.login_btn')
        login_button.click()

        # ログイン処理を待ちます
        time.sleep(2)  # 実際の読み込み時間に応じて調整してください

        # ギフトコードを入力します
        gift_code_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="交換コードを入力してください"]')
        gift_code_input.clear()
        gift_code_input.send_keys(gift_code)

        # 「交換確認」ボタンをクリックします
        exchange_button = driver.find_element(By.CSS_SELECTOR, 'div.exchange_btn')
        exchange_button.click()

        # 成功のログを出力します
        print(f'ID: {player_id} にギフトコード: {gift_code} を正常に送信しました。')

        # 交換処理を待ちます
        time.sleep(3)  # 実際の処理時間に応じて調整してください

        # ポップアップが表示されるか確認し、「決定」ボタンを押して閉じます
        try:
            confirm_button = driver.find_element(By.CSS_SELECTOR, 'div.confirm_btn')
            confirm_button.click()
            print(f'ID: {player_id} のポップアップを閉じました。')
        except Exception as e:
            print(f'ID: {player_id} のポップアップが見つかりませんでした。続行します。')

    except Exception as e:
        # 失敗のログを出力します
        print(f'ID: {player_id} へのギフトコード送信に失敗しました。理由: {str(e)}')

# ブラウザを閉じます
driver.quit()
