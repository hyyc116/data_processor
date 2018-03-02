#coding:utf-8
from util import *

def filed_stats(fk_path):
    ## load the fos mapping
    fos_dict = defaultdict(list)
    for line in open('OCDE_fos.txt'):
        line= line.strip()
        top,second,content = line.split('\t')

        fos_dict[top].append(','.join([second,content]).lower())

    for line in open(fk_path):
        line = line.strip()
        fos,keyword = line.split('\t')

        for top in fos_dict.keys():
            if fos in fos_dict[top]:
                print top+"\t"+fos+"\t"+keyword

if __name__ == '__main__':
    filed_stats(sys.argv[1])