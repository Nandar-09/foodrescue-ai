import streamlit as st

from prediction import predict_waste
from ai_recommendation import generate_ai_recommendation


# ==========================================
# Page settings
# ==========================================

st.set_page_config(
    page_title="FoodRescue AI v1.1",
    page_icon="🍱",
    layout="wide"
)


# ==========================================
# Header
# ==========================================

st.title("🍱 FoodRescue AI v1.1")

st.subheader(
    "AIで食品ロスを減らすスマート販売支援システム"
)

st.write(
    "販売データから売れ残りを予測し、"
    "AIが最適な割引率と販売戦略を提案します。"
)

st.divider()


# ==========================================
# Product information
# ==========================================

st.header("📦 商品情報")

col1, col2 = st.columns(2)

with col1:

    food = st.text_input(
        "商品名",
        value="弁当"
    )

    stock = st.number_input(
        "現在の在庫数",
        min_value=0,
        value=20,
        step=1
    )

    price = st.number_input(
        "商品価格（円）",
        min_value=0,
        value=600,
        step=10
    )


with col2:

    average_sales = st.number_input(
        "平均販売数",
        min_value=0,
        value=12,
        step=1
    )

    hours_remaining = st.number_input(
        "販売終了までの時間",
        min_value=1,
        max_value=24,
        value=4,
        step=1
    )

    weather = st.selectbox(
        "現在の天気",
        [
            "Sunny ☀️",
            "Cloudy ☁️",
            "Rainy 🌧️"
        ]
    )


weather_value = weather.split()[0]

st.divider()


# ==========================================
# AI Prediction button
# ==========================================

if st.button(
    "🤖 AI Prediction",
    type="primary",
    use_container_width=True
):

    # ======================================
    # Step 1: Prediction
    # ======================================

    result = predict_waste(
        stock,
        average_sales,
        hours_remaining,
        weather_value
    )

    discounted_price = round(
        price * (1 - result["discount"] / 100)
    )


    # ======================================
    # Step 2: Prediction result
    # ======================================

    st.header("📊 AI Prediction Result")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "現在の在庫",
            f"{stock}個"
        )

    with col2:
        st.metric(
            "予測販売数",
            f"{result['expected_sales']}個"
        )

    with col3:
        st.metric(
            "予測売れ残り",
            f"{result['leftover']}個"
        )

    with col4:
        st.metric(
            "廃棄リスク",
            result["risk"]
        )


    # ======================================
    # Step 3: Price recommendation
    # ======================================

    st.divider()

    st.header("💰 AI価格提案")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "通常価格",
            f"¥{price}"
        )

    with col2:
        st.metric(
            "推奨割引率",
            f"{result['discount']}%"
        )

    with col3:
        st.metric(
            "割引後価格",
            f"¥{discounted_price}"
        )


    # ======================================
    # Step 4: Prediction summary
    # ======================================

    st.divider()

    st.header("💡 Prediction Summary")

    if result["risk"] == "High":

        st.error(
            f"⚠️ {food}の廃棄リスクが高いです。"
        )

    elif result["risk"] == "Medium":

        st.warning(
            f"⚠️ {food}の売れ残りに注意してください。"
        )

    else:

        st.success(
            f"✅ {food}の廃棄リスクは低いです。"
        )

    st.info(
        f"""
**予測廃棄率:** {result['waste_rate']}%

**予測売れ残り:** 約 {result['leftover']}個

**推奨割引率:** {result['discount']}%

**おすすめ販売価格:** ¥{discounted_price}
"""
    )


    # ======================================
    # Step 5: Graph
    # ======================================

    

    st.divider()

    st.header("📊 在庫・販売予測")

    if stock > 0:
        sales_ratio = min(result["expected_sales"] / stock, 1.0)
        leftover_ratio = min(result["leftover"] / stock, 1.0)
    else:
        sales_ratio = 0
        leftover_ratio = 0

    st.write(f"予測販売数：{result['expected_sales']}個")
    st.progress(sales_ratio)

    st.write(f"予測売れ残り：{result['leftover']}個")
    st.progress(leftover_ratio)


    # ======================================
    # Step 6: OrcaRouter AI Recommendation
    # ======================================

    st.divider()

    st.header("🤖 AI Recommendation")

    with st.spinner(
        "AIが最適な販売戦略を考えています..."
    ):

        try:

            ai_advice = generate_ai_recommendation(
                food,
                stock,
                weather_value,
                result
            )

            if ai_advice:
                st.success(ai_advice)

            else:
                st.warning(
                    "AIから回答を取得できませんでした。"
                )

        except Exception as e:

            st.error(
                "AI Recommendation の取得に失敗しました。"
            )

            st.code(str(e))