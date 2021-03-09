#!/usr/bin/python
import exifread
import sys
import logging
#from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log
import math


def main():
	buf=['Make','Model','DateTime','GPSLatitude','GPSLongitude']
	if (len(sys.argv) < 2 or len(sys.argv) > 2):
		print("Error! - No Image File Specified!")
	elif (len(sys.argv) == 2):
		try:
			file = open(sys.argv[1], 'rb')
			data = process_file(file)
			tag_keys = list(data.keys())
			tag_keys.sort()
			print("Source File:",sys.argv[1])
			#print(tag_keys)
			for i in tag_keys:
				#print(tag_keys[GPSLatitudeRef])
				try:
					if ('Image' in i):
						if(i[6::] in buf and i[6::]=='DateTime'):
							timeval = data[i].printable
						elif(i[6::] in buf):
							print(i[6::],": ",data[i].printable, sep = '')
				except:
					print("%s : %s", i, str(data[i]))
			print("Original Date/Time:", timeval)
			for i in tag_keys:
				if('GPS' in i):
					if(i[4::]=='GPSLatitudeRef'):
						zone = data[i].printable
					if(i[4::]=='GPSLongitudeRef'):
						angle = data[i].printable
			for i in tag_keys:
				try:
					if ('GPS' in i and i[4::] in buf):
						#print(data[i].printable)
						dire = data[i].printable.strip('][').split(', ')						
						nums = dire[2].split('/')						
						if(len(nums)>1):
							quo = float(float(nums[0])/float(nums[1]))								
						else:
							quo = 0
						num = dire[1].split('/')						
						if(len(num)>1):
							q = float(float(num[0])/float(num[1]))
						else:
							q = 0							
						if((i[4::] =='GPSLatitude' and zone == 'S') or (i[4::]=='GPSLongitude' and angle == 'W')):	
							if (quo!=0 and q==0): 
								print(i[7::],": -", dire[0], " degrees, ",float(dire[1])," minutes, ",quo," seconds",sep='')
							elif(quo!=0 and q!=0):
								print(i[7::],": -", dire[0], " degrees, ",float(q)," minutes, ",quo," seconds",sep='')
							elif(quo==0 and q!=0):
								print(i[7::],": -", dire[0], " degrees, ",float(q)," minutes, ",dire[2]," seconds",sep='')
							else:
								print(i[7::],": -", dire[0], " degrees, ",float(dire[1])," minutes, ",dire[2]," seconds",sep='')
						elif(i[4::] =='GPSLatitude' and zone=='N') or (i[4::]=='GPSLongitude' and angle == 'E'):							
							if (quo!=0 and q==0): 
								print(i[7::],": ", dire[0], " degrees, ",float(dire[1])," minutes, ",quo," seconds",sep='')
							elif(quo!=0 and q!=0):
								print(i[7::],": ",dire[0]," degrees, ",float(q)," minutes, ",quo," seconds", sep='')
							elif(quo==0 and q!=0):
								print(i[7::],": ", dire[0], " degrees, ",float(q)," minutes, ",dire[2]," seconds",sep='')
							else:
								print(i[7::],": ", dire[0], " degrees, ",float(dire[1])," minutes, ",dire[2]," seconds",sep='')
				except:
					print("%s : %s", i, str(data[i]))
		except IOError:
			print("Error! - File Not Found!")
if __name__ == '__main__':
	main()
