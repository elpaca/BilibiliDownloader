import utility
import time
import logging
import os
import subprocess

DOWNLOAD_PATH = 'downloads'

class Part(object):
    def __init__(self, cid, title, name, duration):
        self.cid = cid
        self.postTitle = title
        self.name = name
        self.duration = duration
        self.client = utility.getAria2cClientInstance()

    def download(self):
        logging.info('Downloading part: %s %s' % (self.name, self.postTitle))
        segments = utility.getVideoSegmentedLinks(self.cid)
        logging.info('Segments count: %d' % len(segments))
        # preparing info
        filename = '%s - %s' % (self.postTitle, self.name)
        filename = utility.escapeFileName(filename)
        sequence_file = DOWNLOAD_PATH + '\\' + filename + '.txt'
        concated_file = DOWNLOAD_PATH + '\\' + filename + '.flv'
        if not os.path.exists(DOWNLOAD_PATH): os.mkdir(DOWNLOAD_PATH)
        gids = []
        segment_flvs = []
        # start downloading & make list file for combining
        with open(sequence_file, 'w+') as vlist:
            for mirrors in segments:
                gids.append(self.client.addUri(mirrors, {'dir': DOWNLOAD_PATH}))
                # get flv filename
                sample = mirrors[0]
                sample = sample[:sample.index('?')]
                fn = os.path.basename(sample)
                # write to vlist file
                vlist.write("file '%s\\%s'\n" % (DOWNLOAD_PATH, fn))
                segment_flvs.append('%s\\%s' % (DOWNLOAD_PATH, fn))
            vlist.close()
        # wait for tasks
        for gid in gids:
            while self.client.tellStatus(gid)['status'] != 'complete':
                time.sleep(1)
        # combine segments
        logging.info('Combining segments')
        subprocess.check_output(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', sequence_file, '-c', 'copy', concated_file], stderr=subprocess.STDOUT)
        # clean up
        os.remove(sequence_file)
        for tmp in segment_flvs: os.remove(tmp)


        

        
