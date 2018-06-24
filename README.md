# BilibiliDownloader
Use aria2 to download bilibili videos. Multi-part video supported.
## Dependency
+ [ffmpeg](https://ffmpeg.org) - used to concat segments
+ [aria2](https://aria2.github.io/) - downloading videos
## Feature
+ Show basic information of specified video post
+ Download all parts/specified part of a video
+ Batch downloading supported. You can download many posts in one go
+ CID download supported. This is used to download special posts such as bainianji
## Installation
For windows, copy "aria2c.exe" and "ffmpeg.exe" to root directory of the repository. Then create file "aria2c.conf" "start_server.bat". Run "start_server.bat" to start aria2c server. You can also download pre-configured binary in releases. File examples are provided below.
### aria2c.conf
```
enable-rpc=true
rpc-allow-origin-all=true
max-connection-per-server=16
split=256
min-split-size=1M
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

