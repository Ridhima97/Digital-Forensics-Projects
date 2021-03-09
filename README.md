# Digital-Forensics-Projects
Python programs that perform analysis on given files and parse information from them. All programs have been written with Python3. All work is my own, and done by self. 

The repository contains 3 python files:

1) exifParse.py imitates the work of the EXIF tool used to extract information from images. It extracts the make and model of the device that took the photo, as well as the date, time and latitude/longitude of the photo location. Currently, it only works on JPG files. 

2) netParse.py performs network log analysis on a given CSV file. The format of the csv file has to include the following: Time connection established (standard epoch value), Source IP, Destination IP, Source Port, Destination Port, Bytes sent (source to destination), Bytes received (destination to source), and Total bytes transferred. The python code answers the following questions (given sample basic information about infected ports): 
- How many systems on the internal network are infected?
- What are the IP addresses of the infected systems within the network?
- How many C2 servers are infected systems communicating with?
- What are the IP addresses of the C2 servers the infected systems are communicating with?
- What is the earliest date of the first connection to one of the C2 servers?
- What is the total amount of data (in bytes) sent from internal systems to each of the malware C2 servers?

3) historyParse.py performs analysis on a given Google Chrome history database (SQLite). The code answers the following questions: 
- The total number of downloads
- The name of the file which took the longest time to download
- The size of that file (in bytes)
- The number of unique search terms
- The most recent search term
- The date & time of the most recent search

Sample test files for the above programs are given to test the output. 
