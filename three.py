from selenium import webdriver
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()

driver.get("http://www.yunpan.360.cn")

#定位到要右击的元素
right_click = driver.find_element_by_id('xx')
#执行右击操作
ActionChains(driver).context_click(right_click).perform()

#定位到要悬停的元素
above = driver.find_element_by_id('id')
#执行悬停动作
ActionChains(driver).move_to_element(above).perform()

#定位到要双击的元素
double_click = driver.find_element_by_id('id')
ActionChains(driver).double_click(double_click).perform()


#鼠标拖放动作
#定位到要悬停的元素
element = driver.find_element_by_id('id')
#定位元素要移动到的目标位置
target = driver.find_element_by_id('id')
#执行元素的拖放动作
ActionChains(driver).drag_and_drop(element, target).perform()