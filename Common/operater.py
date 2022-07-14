# -*-coding:utf8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *   # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Remote
import random
import sys

def browser(browser="chrome"):
    """
    打开浏览器函数:Firefox、chrome、ie、phantomjs
    """
    # 定义多终端浏览器
    nodes = [
        'http://192.168.25.107:5555/wd/hub',
        'http://192.168.25.49:5555/wd/hub',
        'http://192.168.25.107:5566/wd/hub'
    ]
    x = random.randint(0, 2)

    try:
        if browser == "firefox":
            # profile_dir = r'C:\Users\zlj.SOFT\AppData\Roaming\Mozilla\Firefox\Profiles\xvwm5zbq.default'
            # profile = webdriver.FirefoxProfile(profile_dir)
            # driver = webdriver.Firefox(profile)
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            # Chrome无界面模式
            # chrome_options = Options()
            # chrome_options.add_argument('--headless')
            # driver = webdriver.Chrome(options=chrome_options)

            # 分布式
            # sys.stderr.write(nodes[x])
            # driver = Remote(command_executor=nodes[x],
            #                     desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '',
            #                                           'javascriptEnabled': True})

            # Chrome有界面模式
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser, You can enter 'firefox','chrome','ie' or 'phantomjs'")
    except Exception as msg:
        print("%s" % msg)

class Operater(object):
    """基于原生的selenium 框架做的二次封装。"""

    def __init__(self, driver, *args):
        """
        启动浏览器参数化，默认启动 chrome.
        """
        self.driver = driver

    def open(self, url, t='', timeout=20):
        """
        使用get 打开URL后，最大化窗口，判断 title符合预期
        Usage:
          driver = operater()
          driver.open(url, t='')
        """

        self.driver.get(url)
        # print("URL is %s" % url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_contains(t))
        except TimeoutException:
            print("Open %s title error" % url)
        except Exception as msg:
            print("Error: %s" % msg)

    def find_element(self, locator, timeout=10):
        '''
        定位元素，参数 locator 是元祖类型
        Usage:
        locator = ("id","xxx")
        driver.find_element(locator)
        '''
        element = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        return element
        # try:
        #     element = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        #     return element
        # except BaseException as msg:
        #     print("Error: %s" % msg)


    def find_elements(self, locator, timeout=10):
        '''定位一组元素'''
        elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return elements
        # try:
        #     elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        #     return elements
        # except BaseException as msg:
        #     print("Error: %s" % msg)

    def clear(self, locator):
        """
        点击操作
        Usage:
          locator = ("id", "xxx")
          driver.clear(locator)
        """
        element = self.find_element(locator)
        element.clear()
        # try:
        #     element = self.find_element(locator)
        #     element.clear()
        # except BaseException as msg:
        #     print("Error: %s" % msg)

    def click(self, locator):
        """
        点击操作
        Usage:
          locator = ("id", "xxx")
          driver.click(locator)
        """
        element = self.find_element(locator)
        element.click()
        # try:
        #     element = self.find_element(locator)
        #     element.click()
        # except BaseException as msg:
        #     print("Error: %s" % msg)

    def send_keys(self, locator, text):
        '''
        収送文本，清空后输入
        Usage:
        locator = ("id","xxx")
        driver.send_keys(locator, text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        # try:
        #     element = self.find_element(locator)
        #     element.clear()
        #     element.send_keys(text)
        # except BaseException as msg:
        #     print("Error: %s" % msg)

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        刞断文本在元素里,没定位刡元素迒回 False，定位刡迒回刞
        断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        except:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        刞断元素的 value 值，没定位刡元素迒回 false,定位刡迒回刞
        断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
        except:
            print("元素没定位刡：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''刞断 title 完全等亍'''

        try:
            result = WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_title_contains(self, title, timeout=10):
        '''刞断 title 包吨'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_selected(self, locator, timeout=10):
        '''刞断元素被选中，迒回布尔值,'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.element_located_to_be_selected(locator))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''刞断元素的状态，selected 是期望的参数 true/False
        迒回布尔值'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.element_located_selection_state_to_be(locator, selected))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_alert_present(self, timeout=10):
        '''刞断页面是否有 alert，
        有迒回 alert(注意返里是迒回 alert,丌是 True)
        没有迒回 False'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_visibility(self, locator, timeout=10):
        '''元素可见迒回本身，丌可见迒回 Fasle'''

        try:
            result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_invisibility(self, locator, timeout=10):
        '''可见的元素返回False,不存在的元素见返回True;隐藏的元素返回WebElement'''

        try:
            result = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),"Fail")
        except:
            print("已找到元素")
            return False
        else:
            return result

    def is_clickable(self, locator, timeout=10):
        '''元素可以点击 is_enabled 迒回本身，丌可点击迒回 Fasle'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def is_located(self, locator, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回 False'''
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except:
            print("元素没定位到")
            return False
        else:
            return result

    def move_to_element(self, locator):
        """鼠标悬停操作
        Usage:
          locator = ("id", "xxx")
          driver.move_to_element(locator)
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        # try:
        #     element = self.find_element(locator)
        #     ActionChains(self.driver).move_to_element(element).perform()
        # except:
        #     print("元素没定位到")

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''

        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''

        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        '''通过索引,index 是索引第几个，从 0 开始'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)
        # try:
        #     element = self.find_element(locator)
        #     Select(element).select_by_index(index)
        # except:
        #     print("元素没定位到")

    def select_by_value(self, locator, value):
        '''通过 value 属性'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)
        # try:
        #     element = self.find_element(locator)
        #     Select(element).select_by_value(value)
        # except:
        #     print("元素没定位到")

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)
        # try:
        #     element = self.find_element(locator)
        #     Select(element).select_by_visible_text(text)
        # except:
        #     print("元素没定位到")

    def switch_to_iframe(self, locator):
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def waitClick(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        
    def pageload(self):
        state = self.driver.execute_script("return document.readyState")
        re = (state == "complete")
        return re

    # if __name__ == '__main__':
