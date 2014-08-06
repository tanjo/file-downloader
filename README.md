File Downloader
================

## 概要

ファイルをループさせながらダウンロードしたいなぁという安易な気持ちで作成してしまった

## 使い方

### シンプルなダウンロード

  ```
  dl.py [file]
  ```

### シンプルなダウンロード（ループ）

  [start number] は開始番号で [end number] は終了番号

  ```
  dl.py [prefix] [suffix] [start number] [end number]
  ```

## Invoke にも対応しました

  [pyinvoke/invoke](https://github.com/pyinvoke/invoke)

### 使い方

  ```
  invoke dl --help
  invoke dl --url='url'
  invoke dl --prefix='http://www.sample.' --suffix='.jpg' --start=0 --end=5
  ```
