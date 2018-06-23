from post import Post
import argparse
import logging
import os
import utility


def checkDependences():
    if not os.path.exists('ffmpeg.exe'):
        print('ffmpeg.exe required!')
        return False
    try:
        utility.getAria2cClientInstance().tellActive()
    except:
        print('Failed to connect to aria2c server. Be sure you have started it.')
        return False
    return True


if __name__ == '__main__':
    if not checkDependences():
        quit()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    ap = argparse.ArgumentParser(description='Bilibili Video Downloader')
    ap.add_argument('avid', help='AVID of video to download.')
    ap.add_argument('-d', '--download', action='store_true', help='Download all parts of the video post. You should start the aria2c server manually before downloading.')
    ap.add_argument('-p', '--part', type=int, default=-1, help='Download specific part. Please input sequence number, e.g. 2 for the second part. ')
    args = ap.parse_args()

    avid = args.avid
    if avid.startswith('av'): avid = avid[2:]
    post = Post(avid)
    post.showInfo()

    if args.download:
        if args.part == -1:
            logging.info('Downloading post: %s (%d parts in total)' % (post.title, len(post.parts)))
            for p in post.parts:
                p.download()
        else:
            post.parts[args.part - 1]
