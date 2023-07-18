import feedparser
import requests
import sys
import os
import re
import time
import datetime
from datetime import datetime
import pytz
from unidecode import unidecode
import eventlet
######################################################
#location of RSS html files
htmlDir = "/var/www/html/home/usb/feeds/"
#your timezone
tZone = 'US/Eastern'
#
#use cron to schedule hourly
scheduler = [ 						# referenced in urls[x][0] (line 32)
'06', 							# 0 = daily
'06,12', 						# 1 = twice daily
'06,08,10,12,14,16,18,20,22', 				# 2 = every ~2 hours
'06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23'	# 3 = hourly
]
#
#to find YOUTUBE channel ID RSS url
#   1. Open channel, right click view source
#   2. Ctrl + F "https://www.youtube.com/channel/" to find channel ID
#   3. Add ID to end of "https://www.youtube.com/feeds/videos.xml?channel_id="
#
urls = [ #scheduler[x],name,url
[3,'Hacker News Frontpage','https://hnrss.org/frontpage'],
[3,'Reddit Technology','https://www.reddit.com/r/technology/hot.rss']
]
######################################################
timezone = pytz.timezone(tZone)
localnow = datetime.now(timezone).strftime('%H') 	#Local timezone used for scheduling only
dnow = str(datetime.now().strftime('%H')) 		#we assume RSS using +00:00 UTC timezone in the <updated> block of feed
hnow = str(datetime.now().strftime('%m-%d')) 		#we assume RSS using +00:00 UTC timezone in the <updated> block of feed
print(dnow + "(" + localnow + ") - " + hnow)
urllen = len(urls)
urlrange = range(0,urllen)
for x in urlrange:
	if str(localnow) in (scheduler[(urls[x][0])]):
		try:
			with eventlet.timeout.Timeout(5):
				response = requests.get(urls[x][2])
			parseurl = str(urls[x][2])
			d = feedparser.parse(parseurl)
			dl = []
			fname = urls[x][1].replace(" ","")
			rfile = str(htmlDir) + str(fname) + ".html"
			for post in d.entries:
				v1hrcheck = post.updated_parsed.tm_hour
				if v1hrcheck < (10):
					v1hrstrip = ("0" + str(v1hrcheck))
				else:
					v1hrstrip = str(v1hrcheck)
				v1mincheck = post.updated_parsed.tm_min
				if v1mincheck < (10):
					v1minstrip = ("0" + str(v1mincheck))
				else:
					v1minstrip = str(v1mincheck)
				v1seccheck = post.updated_parsed.tm_sec
				if v1seccheck < (10):
					v1secstrip = ("0" + str(v1seccheck))
				else:
					v1secstrip = str(v1seccheck)
				v1 = (v1hrstrip + "-" + v1minstrip + "-" + v1secstrip)
				v2check = post.updated_parsed.tm_mon
				if v2check < (10):
					v2strip = ("0" + str(v2check))
				else:
					v2strip = str(v2check)
				v2 = v2strip.lstrip("0")
				v3check = post.updated_parsed.tm_mday
				if v3check < (10):
					v3strip = ("0" + str(v3check))
				else:
					v3strip = str(v3check)
				if ((v2strip + "-" + v3strip) == (dnow)) and ((int(hnow) - int(v1hrstrip)) < 2):
					newr = "rn"
				else:
					newr = "rl"
				v3 = v3strip.lstrip("0")
				v4 = post.link
				v4titlePre = post.title
				v4titlePost = unidecode(v4titlePre)
				v5 = (v2strip + "-" + v3strip + "-" + v1)
				v6 = ("<div id=\"" + v5 + "\" class=\"rssdiv\"><div class=\"rssdate\" id=\"" + newr + v2 + "-" + v3 + "\">" + v2strip + "-" + v3strip + " " + v1hrstrip + ":" + v1minstrip + "</div><div class=\"rsslink\" id=\"" + newr + v2 + "-" + v3 + "\"><a href=\"" + v4 + "\" target=\"_blank\">" + v4titlePost + "</a></div><br></div>")
				dl.append(v6)
			dl2 = sorted(dl, reverse=True)
			v7 = str(datetime.today().strftime('%H:%M,%m-%d-%Y'))
			with open(rfile, mode="wt", encoding="utf-8") as myfile:
				myfile.write("<div id=\"rssheadlink\">" + str(urls[x][1]) + "</div><div id=\"rssheadupdate\">Last updated: " + v7 + "</div>")
				myfile.write('\n'.join(dl2))
		except requests.exceptions.ReadTimeout:
			print("READ TIMED OUT -" + urls[x][2])
		except requests.exceptions.ConnectionError:
			print("CONNECT ERROR -" + urls[x][2])
		except eventlet.timeout.Timeout:
			print("TOTAL TIMEOUT -" + urls[x][2])
		except requests.exceptions.RequestException:
			print("OTHER REQUESTS EXCEPTION -" + urls[x][2] + "error")
	else:
		print("time scope incorrect - desired time" + str(scheduler[(urls[x][0])]))
