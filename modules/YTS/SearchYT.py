import urllib.request as ur
import json
def yt_video_search(myKeyword, apiKey):
    qq = myKeyword.encode('utf-8')
    videoIdList = list()

    with ur.urlopen(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=3&q={qq}&type=video&key={apiKey}') as response:
        data = response.read()
        jsonData = json.loads(data)
#        print(jsonData["items"])
        for i in jsonData["items"]:
            videoIdList.append(i["id"]["videoId"])
#        print(videoIdList)
    return videoIdList

def yt_video_return(thisVideoIdList):
    linkList = list()
    for i in thisVideoIdList:
        linkList.append(f'https://www.youtube.com/watch?v={i}')
    return linkList

