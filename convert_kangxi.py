import pyperclip
import time
import argparse


def monitor_clipboad(args):
    print("クリップボードの監視を開始します。終了するにはCtr+Cを押してください。")
    data_dic = load_data()
    if pyperclip.paste() is None:
        last_content = ""
    else:
        last_content = pyperclip.paste()
    while True:
        try:
            current_content = pyperclip.paste()
            if current_content != last_content:
                last_content = current_content
                check(current_content, data_dic, verbose=args.verbose)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.1)


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
    if str is None:
        return
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
    if found:
        pyperclip.copy(converted_str)
        if verbose:
            print(print_str)


def main():
    parser = argparse.ArgumentParser(
        description="クリップボードを監視し、康煕部首を変換する"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()
    monitor_clipboad(args)


if __name__ == "__main__":
    main()
