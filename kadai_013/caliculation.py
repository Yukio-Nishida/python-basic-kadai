def total_calc(price, tax):

    #与えられた引数priceと引数taxを加算し、変数totalに代入する
    total = price + tax

    #変数totalの値を出力する
    print(f"合計金額は{total}円です。")

    #戻り値の設定
    return price + tax

# 関数を呼び出し、引数として購入金額と消費税額(10%分)を渡す
total_calc(1000, (1000 * 0.1))