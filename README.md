# ocrプロジェクト - ChatGPT o4-mini OCR

# このプロジェクトについて
このプロジェクトは、ChatGPTを利用してOCR（Optical Character Recognition）を行うためのPythonスクリプトです。画像ファイルからテキストを抽出し、結果を表示します。
# chatGPT o4-miniの画像認識機能の精度が高いので実装してみました。
# 画像ファイルからOCRでテキストを抽出し、結果を表示するPythonスクリプトです。

# セットアップ
1. リポジトリをクローン
   git clone https://github.com/kazu5150/ocr-project-chatGPT-o4mini.git
2. 仮想環境の作成と有効化
   python3 -m venv venv
   source venv/bin/activate
3. 依存関係のインストール
   pip install -r requirements.txt

# 使い方
1. `.env` ファイルに `OPENAI_API_KEY` を設定
2. `images/input.png` をOCR対象の画像に置き換え
3. スクリプトを実行
   python ocr.py

# ライセンス
MIT
