import pyperclip
import time


def monitor_clipboad():
    data_dic = load_data()
    last_content = ""
    while True:
        try:
            current_content = pyperclip.paste()
            if current_content != last_content:
                last_content = current_content
                check(current_content, data_dic, verbose=True)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.5)


def load_data():
    with open("data.dat", "r") as f:
        data_dic = {}
        for line in f:
            key, value = line.split()
            key = chr(int(key, 16))
            value = chr(int(value, 16))
            data_dic[key] = value
    return data_dic


def check(str, data_dic, verbose=True):
    RED = "\033[31m"  # 赤
    RESET = "\033[0m"  # リセット
    converted_str = ""
    print_str = ""
    found = False
    for c in str:
        if c in data_dic:
            print_str += RED + data_dic[c] + RESET
            converted_str += data_dic[c]
            found = True
        else:
            print_str += c
            converted_str += c
    if verbose and found:
        print(print_str)
        print(converted_str)


if __name__ == "__main__":

    # check("テキスト中の康煕部首を⾒つけてCJK漢字に変換します。", data_dic, verbose=True)
    print("クリップボードの監視を開始します。終了するにはCtr+Cを押してください。")
    monitor_clipboad()
