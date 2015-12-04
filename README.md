# pirouette
![Build](https://travis-ci.org/walidsa3d/pirouette.svg?branch=master)
![downloads](https://img.shields.io/pypi/dm/pirouette.svg)
![license](https://img.shields.io/pypi/l/pirouette.svg)
![version](https://img.shields.io/pypi/v/pirouette.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

loading animation for cli apps

## Install (automatic)
```
$ pip install pirouette
```
## Install (manual)
```
$ git clone 
$ cd pirouette
$ python setup.py install
```
## Usage
```python
>> from pirouette.core import Spinner

>> Spinner().spin()
⠏
>> Spinner().spin(color='red')
⠏
>> Spinner().spin(color='yellow', shape='clock')
🕐

```

## License
MIT