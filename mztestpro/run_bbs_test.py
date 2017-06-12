from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import sys
import os


#定义发送邮件
def send_mail(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'uft-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('zouxiaolu1114@163.com', '19901114yctd')
    smtp.sendmail('zouxiaolu1114@163.com', 'zouxiaolu1114@163.com', msg.as_string())
    smtp.quit()
    print('email has send out!')

#查找测试报告目录，找到最新生成的测试报告文件
def newest_report(testReport):
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(testReport, fn)))
    return os.path.join(testReport, lists[-1])

#执行测试并生成测试报告
def create_test_report(testReport):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'result.html'
    filepath = os.path.join(testReport, filename)
    with open(filepath, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='魅族社区自动化测试报告',
                                description='环境: %s'%sys.platform)
        discover = unittest.defaultTestLoader.discover(start_dir='./bbs/test_case',
                                                       pattern='*_sta.py')
        runner.run(discover)


if __name__ == '__main__':
    create_test_report('./bbs/report')
    file_path = newest_report('./bbs/report')
    send_mail(file_path)