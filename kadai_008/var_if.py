#ランダムな整数をインポート
import random

#変数varに0～50までのランダムな整数を入れる
var = random.randint(0, 50)

#変数varの値を出力
print(var)

#変数varの値が3の倍数なら「Fizz」と出力
if var % 3 == 0:
    print("Fizz")

#5の倍数なら「Buzz」と出力
elif var % 5 == 0:
    print("Buzz")

#3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」と出力
elif var % 15 == 0:
    print("FiZZBuzz")

#どれにも該当しない場合は変数varの値を出力
else:
    print(var)