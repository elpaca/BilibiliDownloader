# BilibiliDownloader
Use aria2 to download bilibili videos. Multi-part video supported.
## Dependency
+ [ffmpeg](https://ffmpeg.org) - used to concat segments
+ [aria2](https://aria2.github.io/) - downloading videos
## Feature
+ Show basic information of specified video post
+ Download all parts/specified part of a video
+ Automatically concat segments
## Installation
For windows, copy "aria2c.exe" and "ffmpeg.exe" to root directory of the repository. Then create file "aria2c.conf""start_server.bat". Examples are provided below.
### aria2c.conf
```enable-rpc=true
rpc-allow-origin-all=true
max-connection-per-server=16
split=256
min-split-size=1M # important 
referer=http://www.bilibili.com/
user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
dir=downloads
```
### start_server.bat
```start aria2c --conf-path aria2c.conf```

## Usage
### Show post information
```bdownload.py av170001```
### Download all parts
```bdownload.py -d av170001```
### Download specified part
```bdownload.py -d -p 1 av170001```

## Known Problem
+ 拜年祭视频无法下载，因为特殊网页的原因。后续添加cid选项手动下载。
