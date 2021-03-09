#!/usr/bin/python

import sqlite3 as lite
import sys
import re
from datetime import datetime
MONTH_DICT = { '01': "Jan", '02': "Feb", '03': "Mar", '04': "Apr" , '05': "May",  '06': "Jun",  '07': "Jul", '08': "Aug" , '09': "Sep", '10': "Oct", '11': "Nov", '12': "Dec"}
if (len(sys.argv) < 2 or len(sys.argv) > 2):
		print("Error! - No History File Specified!")
elif (len(sys.argv) == 2):
	try:
		con = lite.connect(sys.argv[1])
		with con:
			cur = con.cursor()
			cur.execute("SELECT COUNT (DISTINCT id) FROM downloads")
			ans = cur.fetchone()
			print("Source File:", sys.argv[1])
			print ("Total Downloads:", ans[0])
			cur.execute("SELECT current_path, received_bytes from downloads ORDER BY (end_time - start_time) DESC LIMIT 1")
			ans = cur.fetchone()
			lis = ans[0].split("\\")
			print("File Name:",lis[-1])
			print("File Size:",ans[1])
			cur.execute("SELECT COUNT(DISTINCT term) FROM keyword_search_terms")
			ans2 = cur.fetchone()
			print("Unique Search Terms:", ans2[0])
			cur.execute("SELECT urls.title, urls.last_visit_time, keyword_search_terms.term from urls INNER JOIN keyword_search_terms ON keyword_search_terms.url_id=urls.id ORDER BY urls.last_visit_time DESC LIMIT 1")
			ans = cur.fetchone()
			print("Most Recent Search:", ans[2])
			cur.execute("SELECT datetime(urls.last_visit_time/1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') from urls INNER JOIN keyword_search_terms ON keyword_search_terms.url_id=urls.id ORDER BY urls.last_visit_time DESC LIMIT 1")
			ans = cur.fetchone()
			lis2 = re.split("[- ]", ans[0])
			#print(lis2)
			if (lis2[1] in MONTH_DICT):
				month = MONTH_DICT[lis2[1]]
			print("Most Recent Search Date/Time: ", lis2[0],"-",month,"-",lis2[2]," ", lis2[3], sep='')
	except:
		print("Error! - File Not Found!")



