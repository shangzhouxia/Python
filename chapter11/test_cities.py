import unittest
from city_function import get_city_name

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        format_name = get_city_name('shanghai', 'china')
        # print(format_name)
        self.assertEqual(format_name, 'Shanghai, China')

    def test_c_c_p(self):
        format_name = get_city_name('shanghai', 'china', 20000000)
        #print(format_name)
        self.assertEqual(format_name, 'Shanghai, China-Population 20000000')

if __name__ == '__main__':
    unittest.main()

""" 
如果测试结果不对，会有详细的提示，比如下面的大小写不对

Z:\test\python\test>python -u "z:\test\python\test\test_cities.py"
F.
======================================================================
FAIL: test_c_c_p (__main__.CityTestCase.test_c_c_p)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "z:\test\python\test\test_cities.py", line 13, in test_c_c_p
    self.assertEqual(format_name, 'Shanghai, China-population 20000000')
AssertionError: 'Shanghai, China-Population 20000000' != 'Shanghai, China-population 20000000'
- Shanghai, China-Population 20000000
?                 ^
+ Shanghai, China-population 20000000
?  
 """