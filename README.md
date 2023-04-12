# The Money Converter

Python汇率转换工具类，数据来源于[themoneyconverter](https://themoneyconverter.com/zh-CN)

## 快速入门
安装
```shell
pip install themoneyconverter
```

使用

```python
from themoneyconverter import MoneyConverter, Currency


if __name__ == '__main__':
    # 获取1元人民币转换其它货币的汇率
    moneyConverter = MoneyConverter(Currency.CNY.name)
    moneyConverter.refresh()
    rate = moneyConverter.get_rate(Currency.ARS.name)
    print(Currency.ARS.value, rate)
```

执行结果示例
```python
Connected to pydev debugger (build 203.7717.81)
阿根廷比索 30.9827

Process finished with exit code 0
```

代码说明
```python
class MoneyConverter:
    URL_TEMPLATE = 'https://themoneyconverter.com/zh-CN/{source}/{target}?amount=1.00'

    def __init__(self, source='CNY', target='CNY'):
        self.rate = {}
        self.source = source
        self.target = target
        self.updateTime = None
```
source是转出货币，target是转入货币，比如说`moneyConverter = MoneyConverter(Currency.CNY.name)`是1元人民币转换其它货币的汇率，target用默认值即可，目前没什么用

支持以下货币汇率互相转换
+ AED = 阿联酋迪拉姆
+ JPY = 日元
+ ARS = 阿根廷比索
+ KRW = 韩元
+ AUD = 澳元
+ MAD = 摩洛哥迪拉姆
+ BRL = 巴西雷亚尔
+ MXN = 墨西哥比索
+ CAD = 加元
+ NOK = 挪威克朗
+ CHF = 瑞士法郎
+ NZD = 新西兰元
+ CNY = 人民币
+ PHP = 菲律宾比索
+ CZK = 捷克克朗
+ PLN = 波兰兹罗提
+ DKK = 丹麦克朗
+ RUB = 俄罗斯卢布
+ EUR = 欧元
+ SEK = 瑞典克朗
+ GBP = 英镑
+ SGD = 新加坡元
+ HKD = 港元
+ THB = 泰铢
+ HUF = 匈牙利福林
+ TRY = 土耳其里拉
+ ILS = 以色列谢克尔
+ USD = 美元
+ INR = 印度卢比
+ ZAR = 南非南特