from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 初始化浏览器驱动（这里以Chrome为例）
driver = webdriver.Chrome()
url = "https://www.bilibili.com/video/BV1fh411y7R8/?p=48&vd_source=6248bbe156e0f31bc6697c05cf70952c"
# 打开要访问的网页
driver.get(url)  # 替换成你要访问的网页链接

# 定位到ul元素，这里以class为example-ul为例
ul_element = driver.find_element(By.CLASS_NAME, "list-box")

# 模拟滚动并获取数据
data_list = []

while True:
    # 获取当前ul中的数据
    items = ul_element.find_elements(By.TAG_NAME,"li")
    for item in items:
        data_list.append(item.text)

    # 向下滚动一屏幕高度
    ActionChains(driver).send_keys(Keys.DOWN).perform()

    # 等待一小段时间，让新数据加载完成（根据页面加载速度适当调整等待时间）
    time.sleep(1)

    # 检查是否已经滚动到页面底部
    # 这里以页面高度作为判断条件，也可以使用其他方式判断是否到达底部
    current_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    viewport_height = driver.execute_script("return Math.max(document.documentElement.clientHeight, window.innerHeight || 0)")
    if current_height <= viewport_height:
        break

# 输出获取到的数据
for data in data_list:
    print(data)

# 关闭浏览器
driver.quit()
