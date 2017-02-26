
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
import xlrd
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def get_user_number(a):
	browser.get(a)
	time.sleep(5)
	online_users = browser.find_element_by_class_name('users-online').text
	users = online_users.split(" ")
	timestamp = str(datetime.now())
	user_time = [users[0],timestamp]
	return user_time
def get_subreddit_url(row_num):
	workbook = xlrd.open_workbook('subreddits.xls')
	worksheet = workbook.sheet_by_index(0)
	subreddit_url = worksheet.cell_value(rowx=row_num, colx=0)
	subreddit_name = worksheet.cell_value(rowx=row_num, colx=1)
	url_and_name = [subreddit_url, subreddit_name]
	return(url_and_name)
	
	
#Main Code
browser = webdriver.Firefox()
for x in range(1,100):	
	for col in range(0,20):
		file_name = get_subreddit_url(col)	
		workbook = xlwt.Workbook(file_name[1]+'.xls')
		worksheet = workbook.add_sheet("Online Users")
		worksheet.write(0,0,"Time")
		worksheet.write(0,1,"Online Users")
		y= get_user_number(file_name[0])
		worksheet.write(x,0,y[1])
		worksheet.write(x,1,y[0])
		print (y)
		time.sleep(5)
		workbook.save(file_name[1]+'.xls')
		