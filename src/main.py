from selenium import webdriver                                 #using Selenium module
browser = webdriver.Chrome('C:\chromedriver\chromedriver')     #this program uses webdriver for chrome 46. build, you can download more ver from https://sites.google.com/chromium.org/driver/ (download the file and extract chromedriver as current path or change the path)
browser.maximize_window()                                      

outfile = open('content.txt','w',encoding='utf-8')
browser.get('https://www.wikipedia.org')
browser.implicitly_wait(10)
button = browser.find_element_by_css_selector('#js-link-box-en').click()
browser.implicitly_wait(10)
button = browser.find_element_by_link_text('All portals').click()
browser.implicitly_wait(10)
button = browser.find_element_by_link_text('A–Z index').click()
browser.implicitly_wait(10)
button = browser.find_element_by_link_text('M').click()
browser.implicitly_wait(10)
button = browser.find_element_by_link_text('M').click()
browser.implicitly_wait(10)
content = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/div[4]/ul[1]/li[1]/a[1]/span[2]')
content.click()
outfile.writelines(content.text +'\n')
browser.implicitly_wait(10)
content = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/p[3]')
outfile.write(content.text)
browser.implicitly_wait(10)
content = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/div[4]/ul[1]/li[2]/a[1]/span[2]')
content.click()
outfile.writelines('\n\n'+content.text +'\n')
browser.implicitly_wait(10)
content = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/p[4]').text
content += browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/p[5]').text
outfile.writelines(content +'\n')
browser.implicitly_wait(10)
content = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/div[4]/ul[1]/li[3]/a[1]/span[2]')
content.click()
outfile.writelines('\n\n'+content.text +'\n')
browser.implicitly_wait(10)
content = browser.find_elements_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[5]/div[1]/ul[1]/li')
for i in content:
    outfile.writelines(i.text+'\n')
outfile.close()
browser.close()

