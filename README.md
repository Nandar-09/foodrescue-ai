# 🍱 FoodRescue AI v1.1

AIを活用して、食品ロスを削減するためのスマート販売支援アプリです。

商品の在庫数や販売状況などをもとに売れ残りを予測し、AIが適切な割引率や販売戦略を提案します。

---

## 📌 概要

コンビニ、スーパー、飲食店などでは、弁当やパンなどの食品が売れ残り、廃棄されることがあります。

FoodRescue AIでは、以下の情報を入力することで売れ残りを予測します。

* 商品名
* 現在の在庫数
* 平均販売数
* 販売終了までの時間
* 天気
* 商品価格

予測結果をもとに、廃棄リスクや推奨割引率を表示し、さらにAIが具体的な販売戦略を提案します。

---

## ✨ 主な機能

### 📦 商品情報の入力

商品の在庫状況や販売条件を入力できます。

### 📊 売れ残り予測

以下の情報を表示します。

* 予測販売数
* 予測売れ残り数
* 予測廃棄率
* 廃棄リスク

### 💰 AI価格提案

廃棄リスクに応じて、

* 推奨割引率
* 割引後価格

を表示します。

### 📈 在庫・販売予測の可視化

予測販売数と予測売れ残り数を視覚的に確認できます。

### 🤖 AI Recommendation

予測結果をAIが分析し、

* おすすめの割引率
* 今すぐ取るべき行動
* 販売方法
* 食品ロス削減につながる理由

などを提案します。

---

## 🔄 システムの流れ

```text
商品情報を入力
      ↓
売れ残りを予測
      ↓
廃棄リスクを判定
      ↓
推奨割引率を計算
      ↓
OrcaRouter経由でAIを利用
      ↓
AIが販売戦略を提案
      ↓
結果を画面に表示
```

---

## 🛠 使用技術

* Python
* Streamlit
* OrcaRouter API
* OpenAI SDK
* python-dotenv
* Git / GitHub
* Streamlit Community Cloud

---

## 🚀 デモアプリ

FoodRescue AI v1.1 は、Streamlit Community Cloudで公開しています。

https://foodrescue-ai-v11.streamlit.app/

スマートフォンからも利用できます。

---

## 📂 GitHub

Repository:

https://github.com/Nandar-09/foodrescue-ai

最新バージョンは **v1.1 branch** です。

---

## 🔐 セキュリティ対策

APIキーなどの機密情報は、ソースコードに直接記載していません。

ローカル環境では `.env`、Streamlit Community Cloudでは Secrets機能を使用して管理しています。

また、以下のファイルを `.gitignore` に追加しています。

```text
.env
.venv/
__pycache__/
```

これにより、APIキーや不要なローカルファイルがGitHubへ公開されないようにしています。

さらに、商品名、在庫数、商品価格などの入力値をチェックし、不正な値や空の入力によるエラーを防止しています。

AI APIでエラーが発生した場合も、内部エラーの詳細をユーザー画面に表示しないようにしています。

---

## 📁 ファイル構成

```text
foodrescue-ai/
├── app.py
├── prediction.py
├── ai_recommendation.py
├── food_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

* `app.py`：Streamlitによる画面表示・ユーザー入力
* `prediction.py`：販売数、売れ残り、廃棄リスク、割引率の計算
* `ai_recommendation.py`：OrcaRouterを利用したAI販売戦略の生成

---

## ▶️ ローカルでの実行方法

### 1. Repositoryを取得

```bash
git clone https://github.com/Nandar-09/foodrescue-ai.git
```

### 2. Project folderへ移動

```bash
cd foodrescue-ai
```

### 3. Virtual environmentを作成

```bash
python3 -m venv .venv
```

### 4. Virtual environmentを有効化

```bash
source .venv/bin/activate
```

### 5. 必要なライブラリをインストール

```bash
python -m pip install -r requirements.txt
```

### 6. `.env` を作成

```text
ORCAROUTER_API_KEY=YOUR_API_KEY
```

APIキーはGitHubへ公開しないでください。

### 7. Streamlitを起動

```bash
python -m streamlit run app.py
```

---

## 🔄 Version

### v1.0

* 商品情報入力
* 売れ残り予測
* 廃棄リスク判定
* 推奨割引率
* AI Recommendation

### v1.1

* 商品価格の入力
* 割引後価格の表示
* 在庫・販売予測の可視化
* 入力値チェック
* APIエラー表示の安全性向上
* UI改善

---

## 🌱 今後の改善

今後は以下の機能を追加したいと考えています。

* 実際の販売データを利用した需要予測
* 曜日・時間帯を利用した予測
* 天気APIとの自動連携
* 複数商品の一括管理
* 店舗別ダッシュボード
* 売上・廃棄量の履歴管理
* AIによる動的価格最適化
* 食品ロス削減量の可視化

---

## 🎯 目標

FoodRescue AIは、単に売れ残りを予測するだけではなく、

**「予測 → 割引 → 販売行動」**

までAIがサポートすることを目指しています。

食品廃棄を減らしながら、店舗の売上や利益も守ることができる販売支援システムへ発展させていきます。

---

## 👤 Developer

**Swe Lin Nandar**
