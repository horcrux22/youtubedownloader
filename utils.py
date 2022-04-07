import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',type=str,required=True, help='다운로드할 곳')
    parser.add_argument('--url',type=str,required=True, help='유튜브 주소')
    
    opt = parser.parse_args()
    return opt

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir