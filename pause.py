#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class Pause:

    #初始化chrome
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://a.weixin.qq.com")
        #显性等待60s
        WebDriverWait(self.driver,60,0.5).until(
            EC.title_is('微信广告服务商平台')
        )
        self.num = 0
        #保存第一页句柄
        self.h = self.driver.current_window_handle
    # 进入广告服务商初始界面
    def again(self):
        self.driver.get("https://a.weixin.qq.com/client")

    #传入公众号原始ID
    def put_ID(self,str):
        #输入原始ID
        self.wait_class_name("TextInput_new__input-3wfiz")
        self.find_class_name("TextInput_new__input-3wfiz").send_keys(str)

    #通过link_text定位
    def find_link_text(self, str):
        mouse = self.driver.find_element_by_link_text(str)
        ActionChains(self.driver).move_to_element(mouse).perform()
        mouse.click()
        return mouse

    #通过class_name定位
    def find_class_name(self, str):
        mouse = self.driver.find_element_by_class_name(str)
        ActionChains(self.driver).move_to_element(mouse).perform()
        mouse.click()
        return mouse

    #通过css_selector定位
    def find_css_selector(self, str):
        mouse = self.driver.find_element_by_css_selector(str)
        ActionChains(self.driver).move_to_element(mouse).perform()
        mouse.click()
        return mouse

    # 通过xpath定位
    def find_xpath(self,str):
        mouse = self.driver.find_element_by_xpath(str)
        ActionChains(self.driver).move_to_element(mouse).perform()
        action = ActionChains(self.driver)
        action.click(mouse).perform()
        return mouse

    #切换到当前窗口
    def changeWindow(self):
        try:
            # 定义所有句柄
            all_h = self.driver.window_handles
            #判断句柄,不等于首页就切换
            for i in all_h:
                if i != self.h:
                    self.driver.switch_to.window(i)
        except Exception:
            print("未切换到当前窗口")

    #创建等待text方法
    def wait_text(self,str):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, str))
        )

    #创建等待class_name方法
    def wait_class_name(self,str):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, str))
        )

    #创建等待css_selector方法
    def wait_selector(self,str):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, str))
        )

    #创建等待xpath方法
    def wait_xpath(self,str):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, str))
        )

     # 处理弹出框
    def alert(self):
        try:
            result = EC.alert_is_present()(self.driver)
            while result:
                result.accept()
        except Exception:
            pass

    #校验值是否为暂无数据
    def validate_xpath(self):
        try:
            time.sleep(0.5)
            s = self.driver.find_element_by_xpath("//div[@class=\"Table_new__loading-PVDQT\"]/div").text
            if s == "暂无数据":
                return True
            else:
                return False
        except Exception:
            pass

    #校验值第4个位置是否为删除计划
    # def validate_selector(self):
    #     try:
    #         # time.sleep(0.5)
    #         d = self.driver.find_elements_by_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)").text
    #         if d == "删除计划":
    #             return True
    #         else:
    #             return False
    #     except Exception:
    #         pass

    #传入公众号原始ID->点击推广我的公众号
    def clickMyWechat(self,id):
        #进入服务商界面
        self.again()
        # 处理确认消息框
        self.alert()
        self.put_ID(id)
        # 点击查询按钮
        self.alert()
        self.wait_class_name("TextInput_new__icon-2b8st")
        self.find_class_name("TextInput_new__icon-2b8st")
        self.wait_text("广告投放")

        # 点击广告投放
        self.find_link_text("广告投放")

        try:
            self.num += 1
            if self.num == 1:
                self.driver.close()
        except Exception:
            pass

         #切换到当前窗口
        self.changeWindow()


        # 点击 投放中
        try:
            self.wait_class_name("ui-c-green")
            self.find_class_name("ui-c-green")
        except Exception:
            print("tou fang zhonng error")
            self.find_class_name("ui-c-green")

        self.wait_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div[3]/table/thead/tr/th[2]/div/div[2]/*[name()=\'svg\']/*[name()='path']")
        # time.sleep(1)
    #暂停投放
    def pause_ad_before(self):
        # 点击状态旁选择框
        self.find_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div[3]/table/thead/tr/th[2]/div/div[2]/*[name()=\'svg\']/*[name()='path']")

        self.wait_selector("li.Table_new__radio_list-PrjiB:nth-child(3)")

        # 点击待投放
        self.find_css_selector("li.Table_new__radio_list-PrjiB:nth-child(3)")

    def pause_ad(self):
        # 点击操作
        time.sleep(0.5)
        self.wait_selector(".Table_new__wrapper-3l9iP > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.find_css_selector(".Table_new__wrapper-3l9iP > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.wait_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")

        #点击暂停投放
        time.sleep(0.5)
        self.find_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
        self.wait_selector("button.withModal__btn-3E823:nth-child(1)")
        # 弹窗点击确定
        self.find_css_selector("button.withModal__btn-3E823:nth-child(1)")

    #删除计划
    def delete_ad_before(self):
        # 点击状态旁选择框
        self.find_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div[3]/table/thead/tr/th[2]/div/div[2]/*[name()=\'svg\']/*[name()='path']")
        self.wait_selector("li.Table_new__radio_list-PrjiB:nth-child(7) > label:nth-child(1)")

        #点击未通过
        self.find_css_selector('li.Table_new__radio_list-PrjiB:nth-child(7) > label:nth-child(1)')

    def delete_ad(self):
        # 点击操作
        time.sleep(0.5)
        self.wait_selector(".Table_new__wrapper-3l9iP > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.find_css_selector(".Table_new__wrapper-3l9iP > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.wait_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")

        time.sleep(0.5)
        self.find_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")

        # # 点击删除计划
        # time.sleep(0.5)
        # try:
        #     if self.validate_selector():
        #         self.wait_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")
        #         self.find_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")
        #     else:
        #         self.wait_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
        #         self.find_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
        # except Exception:
        #     self.find_css_selector(".Scrollbar__content-1Whco > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")

        # 弹窗点击确定
        self.wait_selector("button.withModal__btn-3E823:nth-child(1)")
        self.find_css_selector("button.withModal__btn-3E823:nth-child(1)")

    def auto_ad_before(self,operate):
        #为了循环跳出进行的前置操作
        if operate == "暂停":
            self.pause_ad_before()
        elif operate == "删除":
            self.delete_ad_before()

    def auto_ad(self,operate):
        #判断操作类型,进行后置操作
        if operate == "暂停":
            self.pause_ad()
        elif operate == "删除":
            self.delete_ad()





















