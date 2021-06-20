from selenium import webdriver
import requests
import json
import time
def get_cookies():
    browser = webdriver.Chrome()
    browser.get("https://user.qzone.qq.com/xxx/infocenter")# xxx 改为qq账号
    input("请登陆后按Enter")
    print(browser.get_cookies())
    cookie={}
    for i in browser.get_cookies():
        cookie[i["name"]] = i["value"]
    with open("cookies.txt","w") as f:
        f.write(json.dumps(cookie))
    # time.sleep(5)
    # button = browser.find_element_by_xpath('//*[@id="switcher_plogin"]')
    # button.click()

    #browser.close()
def get_content():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    with open("cookies.txt","r")as f:
        cookies = f.read()
        cookies = json.loads(cookies)
    session = requests.session()
    html = session.get("https://user.qzone.qq.com/xxx/infocenter",headers={"User-Agent":user_agent},cookies=cookies) # xxx改为qq账号
    print(html.text)

if __name__ == "__main__":
	get_cookies()
	get_content()