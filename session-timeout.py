#!/usr/bin/env python3

import requests
import re
import time
import datetime as dt
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the targets and parameters
url = "https://example.com/testpage"

headers = {
  'Connection': 'close',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'en-US,en;q=0.9',
  }

cookies = {
  'JSESSIONID':'id',
  }

# Set timeout condition: keywords in HTTP response eg. Please Login
timeoutMsg = "User Name"

# Set timeout condition: HTTP status in HTTP response eg. 302
timeoutStatus = 200

# Set time increment, default 10 mins
increment = dt.timedelta(minutes=10)

def validator(req, next_time):

  #print('status_code:', req.status_code)
  #print('is_redirect:', req.is_redirect)
  #print('req.text:', req.text)

  match = re.search(timeoutMsg, req.text)

  if(timeoutStatus==req.status_code and match):
    print("Catched! Idle sesstion will timeout within {0:.0f} minutes".format(next_time.seconds / 60))
    return False

  else:
    return True
    
def scheduler(send_time):

  next_time = send_time - dt.datetime.now() + dt.timedelta(seconds=1)
  print("Next request will be sent in {0:.0f} minutes".format(next_time.seconds / 60))
  time.sleep(next_time.seconds)

  try:
    req = requests.get(url, headers=headers, cookies=cookies, verify=False)
    print("A request sent at " + time.strftime("%H:%M:%S", time.localtime()))
    return validator(req, next_time)

  except Exception as error:
    print("Something went wrong" + error)
    return False

print("Testing target is " + url)
print("[Session Timeout Test start at " + time.strftime("%H:%M:%S", time.localtime()) + "]")

#True: session-alive 
#False: session-terminated

send_time = dt.datetime.now()

interval = increment

while scheduler(send_time): 
  
  send_time = dt.datetime.now() + interval

  interval = interval + increment

print("[Session Timeout Test stop at ", time.strftime("%H:%M:%S", time.localtime()) + "]")
