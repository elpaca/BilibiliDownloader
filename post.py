import logging
import time
import datetime
import utility
from part import Part

# bilibili 投稿类 包含视频分p信息
class Post(object):
    def __init__(self, avid):
        logging.info('downloading post info ...')
        initinfo = utility.getPostInfo(str(avid))
        if initinfo == None:
            logging.error('Failed to get video info. Maybe non-exists.')
            quit()
        self.avid = initinfo['aid']
        self.title = initinfo['videoData']['title']
        self.desc = initinfo['videoData']['desc']
        self.duration = utility.durationToTime(initinfo['videoData']['duration'])
        self.pubdate = time.localtime(initinfo['videoData']['pubdate'])
        self.authorName = initinfo['upData']['name']
        self.authorUID = initinfo['upData']['mid']
        self.parts = []
        for p in initinfo['videoData']['pages']:
            part = Part(p['cid'], self.title, p['part'], utility.durationToTime(p['duration']))
            self.parts.append(part)
        
    def showInfo(self):
        print('bilibili av%s %s %s' % (self.avid, self.duration, self.authorName))
        print('%s' % self.title)
        print('\n' + self.desc + '\n')
        print('Parts: (%d in total)' % len(self.parts))
        for p in self.parts:
            print('    %d %s %s' % (p.cid, p.duration, p.name))