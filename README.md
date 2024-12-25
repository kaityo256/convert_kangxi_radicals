# クリップボードを監視して康煕部首を変換するスクリプト

## 概要

実行するとクリップボードを監視し、康煕部首が混ざったテキストがクリップボードにコピーされるとCJK漢字に変換してコピーしなおすPythonスクリプトです。

## 使い方

`argparse`と`pyperclip`が必要なので、例えばvenvでインストールしてください。

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install argparse pyperclip
```

実行すると、以下のような表示になります。

```sh
$ python3 convert_kangxi.py -v
クリップボードの監視を開始します。終了するにはCtr+Cを押してください。
```

この状態ではクリップボードを監視し、クリップボードに康煕部首を含むテキストが入ったことを検出すると、それをCJK漢字に変換してコピーしなおします。`-v`もしくは`--verbose`をつけると、康煕部首を見つけた時にそこを赤くして表示します。

## サンプルテキスト

```txt
テキスト中の康煕部首を⾒つけてCJK漢字に変換します。
今⽇は良い天気です。
⽉曜⽇にはバイトがあります。
⽟⽯混交
```

```sh
python3 convert_kangxi.py -v
```

として実行して上記のテキストをコピーすると、康煕部首を検出していることがわかります。

![fig/screenshot.png](fig/screenshot.png)

## 謝辞

康煕部首とCJK漢字のユニコード対応表は[こちらのブログ](https://imabari.hateblo.jp/entry/2020/08/03/220407)で配布されている[こちらのデータ(Google Spreadsheet)](https://docs.google.com/spreadsheets/d/1rKTSCyWkeMEJ-tp9Fr95UjH-NL-xliVX-gu69-WnX3c/edit?usp=sharing)を利用させていただきました。

## ライセンス

MIT

