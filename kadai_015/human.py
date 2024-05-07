class Human:
    def __init__(self):
        self.name = ""

    # メソッドを定義する(名前)
    def printInfo(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

    # メソッドを定義する(年齢)
    def printInfo(self, age):
        self.age = age

    def print_info(self):
        print(self.age)

# インスタンス化する
yukio = Human()
age = Human()

# メソッドにアクセスして実行する(名前)
yukio.printInfo("幸央")
yukio.print_info()

# メソッドにアクセスして実行する(年齢)
age.printInfo(41)
age.print_info()
