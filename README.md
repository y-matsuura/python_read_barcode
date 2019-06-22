# pyzbar ではまった
https://pypi.org/project/pyzbar/

## 結局のところ
`pip install pyzbar`
だけでは読み込めなかった。

### ので、すべてinstallした
```
$ brew install zbar
$ sudo apt install libzbar0
$ pip install pyzbar
$ pip install pyzbar[scripts]
```
