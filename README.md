# Seleniumを使用したギフトコード自動送信

このプロジェクトは、Selenium WebDriverを使用して、ウェブサイトにギフトコードを自動的に送信するプロセスを自動化します。スクリプトは、ファイルからユーザーIDを読み込み、各ユーザーのアカウントにあらかじめ定義されたギフトコードを送信します。

## 目次
- [前提条件](#前提条件)
- [インストール](#インストール)
- [使い方](#使い方)
- [ファイル](#ファイル)
- [トラブルシューティング](#トラブルシューティング)
- [ライセンス](#ライセンス)

## 前提条件

以下がシステムにインストールされていることを確認してください：

- Python 3.x
- Google Chrome（最新バージョン）
- ChromeDriver（Chromeのバージョンと一致している必要があります）

## インストール

1. **リポジトリをクローンします：**

   ```bash
   git clone <リポジトリURL>
   cd <リポジトリディレクトリ>
   ```

2. **必要なPythonパッケージをインストールします：**

    pipを使用して、必要な依存関係をインストールします：
    ```bash
    pip install selenium
    ```

3. **ChromeDriverのパスを設定します：**

    スクリプト内のchromedriverパスを更新します：
    ```python
    chrome_driver_path = '/opt/homebrew/bin/chromedriver'  # 必要に応じてこのパスを更新してください
    ```

## 使い方

### IDとギフトコードファイルを準備します

- **`id.txt`**: ユーザーIDが1行ごとに記載されたテキストファイル。
- **`gitcode.txt`**: 適用するギフトコードが記載されたテキストファイル。

これらのファイルをスクリプトと同じディレクトリに配置してください。

### スクリプトを実行します

以下のコマンドでPythonスクリプトを実行します：

```bash
python selenium_script.py
```

## ログ出力

スクリプトは、各ギフトコード送信の成功または失敗をコンソールに出力します。

## ファイル

- **`selenium_script.py`**: ギフトコード送信プロセスを自動化するメインスクリプト。
- **`id.txt`**: ユーザーIDが記載されたテキストファイル。
- **`gitcode.txt`**: ギフトコードが記載されたテキストファイル。

## シーケンス図

以下のシーケンス図は、ギフトコード送信プロセスの手順を示しています。

```mermaid
sequenceDiagram
    participant User
    participant Script as Selenium Script
    participant Browser as Web Browser
    participant Website as Giftcode Website

    User->>Script: Run python selenium_script.py
    Script->>Script: Read ID and giftcode files
    Script->>Browser: Launch Web Browser
    Browser->>Website: Navigate to Giftcode Website
    Script->>Website: Enter ID and Giftcode
    Script->>Website: Click Submit
    Website-->>Script: Return success/failure response
    Script->>User: Display Result
```

## トラブルシューティング

- **ChromeDriverのバージョン不一致**: ChromeDriverのバージョンがインストールされているGoogle Chromeのバージョンと一致していることを確認してください。Chromeのバージョンはブラウザの設定で確認でき、対応するChromeDriverは[こちら](https://sites.google.com/chromium.org/driver/)からダウンロードできます。

- **ポップアップ処理**: スクリプトは「この報酬はすでに受け取られています」といったポップアップやエラーを処理します。サイトの構造が変更された場合、問題が発生する可能性がありますので、その際は修正が必要です。

- **タイムアウト**: ページの読み込みが遅い場合などにスクリプトが失敗することがあります。この場合、スクリプト内のスリープ時間を増やすと改善されることがあります。
