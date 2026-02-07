# 1.「hello world」と出力
print("hello world")


# 2.greet関数を実装し「こんにちは」と出力。関数を呼び出して実際に出力させる
def greet():
    print("こんにちは")

greet()


# 3.nameを引数にとり、「私の名前は{name}です」と出力するprint_name関数を実装し、関数を呼び出す
def print_name(name):
    print(f"私の名前は{name}です")

print_name("おにちゃん@62期")


# 4.「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、戻り値をprint関数で出力
def get_greet():
    return "おはようございます"

print(get_greet())


# 5.a, bを引数にとり、その足し算の結果を戻り値として返すadd関数を実装し、関数を呼び出して結果をprint関数で出力
def add(a, b):
    return a + b

print(add(3, 25))