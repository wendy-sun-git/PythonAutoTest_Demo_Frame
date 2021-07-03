### 架构
Python+Selenium+Unittest+ddt+HTMLTestRunner数据驱动测试框架

参考：https://zhuanlan.zhihu.com/p/194268154


1、Business：公共业务模块，如登录模块，可以把登录模块进行封装供调用

2、Common：与业务无关的公共模块，如对Selenium的二次封装，方便后期的调用，还有一些工具类，如在读取数据时需要对读取文件进行封装

3、PageOBject：页面元素的封装，这个根据自己公司系统的业务去做分层封装

4、report：测试报告

5、TestCase：测试用例层

6、TestData：测试数据，对应用例的数据都是在这里去取

7、TestSuite：测试套件

8、conf.ini：浏览器配置文件

9、runner.py：整体运行文件