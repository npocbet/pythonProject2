import argparse
import os
import shutil

import schedule as schedule
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-s", help='source folder')
parser.add_argument("-d", help='destinition folder')
parser.add_argument('--log', default='log.txt', type=argparse.FileType('w+'),
                    help='the file where converted data should be written')

args = parser.parse_args()

# python main.py -s ./1/ -d ./2/
def move_files():
    try:
        args.log.write(''.join([f'file {i} is moved to remote at {datetime.now()} \n'
                                for i in os.listdir(f'{args.s}')]))
        # args.log.close()
        # os.system(f'mv {args.s}* {args.d}')
        for i in os.listdir(f'{args.s}'):
            # print(i)
            shutil.move(args.s + i, args.d + i)

    except Exception as e:
        print(e)


if args.s and args.d:
    schedule.every().minute.do(move_files)
    while True:
        schedule.run_pending()
