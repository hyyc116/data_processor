#coding:utf-8

from util import *


def extract_keywords_from_single_file(single_file):
    for line in open(single_file):
        line = line.strip()
        paper = json.loads(line)
        if paper['lang']=='en':
            print paper['fos'],paper['keywords']


def extract_keywords_from_dir(dir_path):
    for single_file in os.listdir(dir_path):
        single_file_path = dir_path+'/'+single_file
        extract_keywords_from_single_file(single_file_path)



if __name__ == '__main__':
    extract_keywords_from_single_file(sys.argv[1])