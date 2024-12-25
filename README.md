# クリップボード監視康煕部首変換スクリプト

## 概要

実行するとクリップボードを監視し、康煕部首が混ざったテキストがクリップボードにコピーされるとCJK漢字に変換してコピーしなおすPythonスクリプトです。

## 使い方

`keyboard`と`pyperclip`が必要なので、例えばvenvでインストールしてください。

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pyperclip keyboard
```

実行すると、クリップボードを監視し、康煕部首が混ざったテキストを検出するとその旨を表示してCJK漢字に変換したテキストをクリップボードにコピーしなおしてくれます。

## サンプルテキスト

```txt
テキスト中の康煕部首を⾒つけてCJK漢字に変換します。
今⽇は良い天気です。
```
