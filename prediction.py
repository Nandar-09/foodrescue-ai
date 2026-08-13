def predict_waste(stock, average_sales, hours_remaining, weather):

    # 販売終了までの時間を考慮
    if hours_remaining <= 3:
        expected_sales = average_sales * 0.8
    elif hours_remaining <= 5:
        expected_sales = average_sales
    else:
        expected_sales = average_sales * 1.1

    # 天気を考慮
    if weather == "Rainy":
        expected_sales *= 0.8
    elif weather == "Sunny":
        expected_sales *= 1.1

    expected_sales = round(expected_sales)

    # 売れ残り予測
    leftover = max(0, stock - expected_sales)

    # 廃棄率
    waste_rate = leftover / stock if stock > 0 else 0

    # 廃棄リスクと推奨割引率
    if waste_rate >= 0.5:
        risk = "High"
        discount = 30
    elif waste_rate >= 0.25:
        risk = "Medium"
        discount = 20
    else:
        risk = "Low"
        discount = 10

    return {
        "expected_sales": expected_sales,
        "leftover": leftover,
        "waste_rate": round(waste_rate * 100, 1),
        "risk": risk,
        "discount": discount
    }