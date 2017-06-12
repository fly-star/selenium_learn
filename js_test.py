from selenium import webdriver
import os, time

driver = webdriver.Firefox()

driver.get('file:///' + os.path.abspath('textarea_test.html'))

text = 'input text'
js = '''var sum = document.getElementById('id');
        sum.value = '{}';'''.format(text)

driver.execute_script(js)

time.sleep(3)

driver.quit()
