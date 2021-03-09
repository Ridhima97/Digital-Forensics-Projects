#!/usr/bin/python
import csv
import sys
import operator
import datetime
import re

MONTH_DICT = { '01': "Jan", '02': "Feb", '03': "Mar", '04': "Apr" , '05': "May",  '06': "Jun",  '07': "Jul", '08': "Aug" , '09': "Sep", '10': "Oct", '11': "Nov", '12': "Dec"}
if (len(sys.argv) < 2 or len(sys.argv) > 2):
		print("Error! - No Log File Specified!")
elif (len(sys.argv)==2):
	try:
		with open(sys.argv[1]) as csv_file:
			reader = csv.reader(csv_file, delimiter=',')
			ipdict={}
			iplist=[]
			plist=[]
			flist=[]
			slist=[]
			conn=0
			print("Source File:",sys.argv[1])
			for row in reader:
				if(row[4] in ['1337', '1338', '1339', '1340']):
					if (row[1] not in iplist):
						iplist.append(row[1])
					if (row[2] not in slist and row[1] in iplist):
						slist.append(row[2])
					if(conn==0):
						conn=row[0]
			for i in iplist:
				plist.append(i.split("."))
			plist.sort(key= lambda plist: int(plist[3]))
			for i in plist:
				s="."
				s = s.join(i)
				flist.append(s)
			print("Systems Infected:",len(flist))
			print("Infected System IPs:\n",flist, sep='')
			print("C2 Servers:",len(slist))
			plist.clear()
			flist.clear()
			for i in slist:
				plist.append(i.split("."))
			plist.sort(key=operator.itemgetter(1,2,3))
			#print(plist)
			for i in plist:
				s="."
				s = s.join(i)
				flist.append(s)
			print("C2 Server IPs:\n",flist, sep='')
			ans = datetime.datetime.utcfromtimestamp(float(conn)).strftime('%Y-%m-%d %H:%M:%S')
			#print(ans)	
			lis2 = re.split("[- ]", ans)
			#print(lis2)
			if (lis2[1] in MONTH_DICT):
				month = MONTH_DICT[lis2[1]]
			print("First C2 Connection: ", lis2[0],"-",month,"-",lis2[2]," ", lis2[3]," UTC", sep='' )
			csv_file.seek(0)
			for row in reader:
				if(row[2] in flist and (row[2] not in ipdict.keys())):
					ipdict[row[2]] = int(row[5])
				elif(row[2] in flist and (row[2] in ipdict.keys())):
					ipdict[row[2]] +=int(row[5])
			fdict = sorted(ipdict.items(), key=operator.itemgetter(1),reverse=True)
			print("C2 Data Totals:",fdict)
	except:
		print("Error! - File Not Found!")
















