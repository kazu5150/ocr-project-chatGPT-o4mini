#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import base64
import openai
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()


def ocr_image(image_path: str) -> str:
    """
    指定した画像ファイルからテキストを抽出して返す。
    """
    # 1. 画像を読み込み、base64 にエンコード
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    
    # 2. データ URI を作成（拡張子から MIME タイプを推測）
    ext = os.path.splitext(image_path)[1].lower().lstrip(".")
    mime = f"image/{ext if ext != 'jpg' else 'jpeg'}"
    data_uri = f"data:{mime};base64,{img_b64}"
    
    # 3. ChatCompletion API に送信するメッセージを構築
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text",      "text": "この画像からテキストを抽出し,構造化して表形式で出力してください。"},
                {"type": "image_url", "image_url": {"url": data_uri}}
            ]
        }
    ]
    
    # 4. API 呼び出し
    response = openai.chat.completions.create(
        model="gpt-4o-mini",   # OpenAI o4-mini モデル
        messages=messages,
        temperature=0.0,       # OCR は創作を抑えたいので 0.0
        max_tokens=2048,
    )
    
    # 5. 結果のテキスト部分を返却
    return response.choices[0].message.content


def main():
    # 環境変数から API キーを取得
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません。")

    # OCR したいローカル画像ファイルのパス
    image_path = "images/input.png"
    
    # OCR 実行
    extracted_text = ocr_image(image_path)
    
    # 結果を表示
    print("----- 抽出されたテキスト -----")
    print(extracted_text)


if __name__ == "__main__":
    main()
