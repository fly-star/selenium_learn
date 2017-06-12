from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox()
driver.get('http://videojs.com')

# video = driver.find_element_by_xpath('body/section[1]/div/video')
video = driver.find_element_by_id('preview-player_html5_api')

#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

#播放视频
print('start')
driver.execute_script('return arguments[0].play();', video)

#播放15秒
sleep(15)

driver.get_screenshot_as_file(os.path.join(os.getcwd(), 'test.jpg'))

#暂停视频
print('stop')
driver.execute_script('arguments[0].pause();', video)

driver.quit()