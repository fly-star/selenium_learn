from selenium import webdriver
import os


#截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(base_dir)
    file_path = os.path.join(base_dir, 'report', 'image', file_name)
    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()

