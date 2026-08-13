import streamlit as st

from prediction import predict_waste
from ai_recommendation import generate_ai_recommendation


# ==========================================
# Page settings
# ==========================================

st.set_page_config(
    page_title="FoodRescue AI",
    page_icon="🍱",
    layout="wide"
)


# ==========================================
# Header
# ==========================================

st.title("🍱 FoodRescue AI")

st.subheader(
    "AIで食品ロスを減らすスマート販売支援システム"
)

st.write(
    "販売データから売れ残りを予測し、"
    "AIが最適な販売戦略を提案します。"
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
    # Step 3: Prediction summary
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

**推奨割引率:** {result['discount']}%

**予測売れ残り:** 約 {result['leftover']}個
"""
    )


    # ======================================
    # Step 4: OrcaRouter AI Recommendation
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