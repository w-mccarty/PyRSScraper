import feedparser
import requests
import sys
import os
import re
import time
import datetime
from datetime import datetime
from unidecode import unidecode
import eventlet

urls = [
'https://www.reddit.com/r/news/hot.rss',
]

for x in urls:
	try:
		with eventlet.timeout.Timeout(5):
			response = requests.get(x)
		parseurl = str(x)
		d = feedparser.parse(parseurl)
		r2 = re.sub(r'[?|$|.| |!|,|:|"|/|\|>|<|-|&|%|*|#|â€“|-|-|_|-]',r'',parseurl) 
		r21 = r2.replace("www", "")
		r22 = r21.replace("https", "")
		r23 = r22.replace("http", "")
		r24 = r23.replace("com", "")
		r25 = r24.replace("feeds", "")
		r26 = r25.replace("feed", "")
		r27 = r26.replace("rss", "")
		r3 = r27[0:24]
		dl = []
		rfile = "/var/www/html/feeds/" + r3 + ".html"
		dnow = str(datetime.today().strftime('%m-%d'))
		hnow = str(datetime.today().strftime('%H'))
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
			myfile.write("<div id=\"rssheadlink\">" + x + "</div><div id=\"rssheadupdate\">Last updated: " + v7 + "</div>")
			myfile.write('\n'.join(dl2))
	except requests.exceptions.ReadTimeout:
		print("READ TIMED OUT -" + x)
	except requests.exceptions.ConnectionError:
		print("CONNECT ERROR -" + x)
	except eventlet.timeout.Timeout:
		print("TOTAL TIMEOUT -" + x)
	except requests.exceptions.RequestException:
		print("OTHER REQUESTS EXCEPTION -" + x + "error")
