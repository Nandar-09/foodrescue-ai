import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ORCAROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.orcarouter.ai/v1"
)


def generate_ai_recommendation(food, stock, weather, prediction):

    prompt = f"""
あなたは食品ロス削減を支援するAIアドバイザーです。

以下の店舗データを分析してください。

商品名: {food}
現在の在庫数: {stock}個
天気: {weather}
予測販売数: {prediction['expected_sales']}個
予測売れ残り: {prediction['leftover']}個
予測廃棄率: {prediction['waste_rate']}%
廃棄リスク: {prediction['risk']}
推奨割引率: {prediction['discount']}%

店舗スタッフ向けに、
・現在の状況
・おすすめの割引
・今すぐ取るべき行動
・食品ロス削減につながる理由

を含めて、短く分かりやすい日本語で回答してください。
"""

    response = client.chat.completions.create(
        model="orcarouter/auto",
        messages=[
            {
                "role": "system",
                "content": "あなたは食品ロス削減の専門AIアドバイザーです。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content