#!/usr/bin/python3
import requests
import os
import sys
import time

if len(sys.argv) == 1:
	print('You forgot post link')
	exit()

post_url = sys.argv[1] + '.json'

headers = {
	'User-Agent': 'My User Agent 1.0',
	'From': 'testyouremail@domain.com'
}
url = post_url + ".json"
data = requests.get(url, headers=headers).json()
media_data = data[0]["data"]["children"][0]["data"]["media"]
title = data[0]["data"]["children"][0]["data"]["title"]

video_url = media_data["reddit_video"]["fallback_url"]
audio_url = video_url.split("DASH_")[0] + "DASH_audio.mp4"

os.system("curl -o video.mp4 {}".format(video_url))
os.system("curl -o audio.mp4 {}".format(audio_url))

while True:
	if os.path.exists('video.mp4') and os.path.exists('audio.mp4'): break
	time.sleep(0.5)

video_path  = title+".mp4"

os.system("ffmpeg -y -i video.mp4 -i audio.mp4 -c:v copy -c:a aac '"+video_path+"'")
os.system("rm video.mp4;rm audio.mp4") 
