# 与えられた引数$priceに消費税10%分を加算し、その値を出力する関数を定義する
def total_calc(price):
    # 与えられた引数priceにを消費税額を加算し、変数totalに代入する
    total = price + (price * 0.1)

    # 変数totalの値を出力する
    print(f"合計は{total}円です。")

# 関数を呼び出し、引数として購入金額を渡す
total_calc(1000)