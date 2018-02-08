#coding:utf-8

from util import *




def extract_keywords_from_single_file(single_file):
    fos_keyword_freq = defaultdict(lambda:defaultdict(int))
    sub_progress=0
    for line in open(single_file):

        sub_progress+=1

        if sub_progress%10000==0:
            logging.info('sub progress: {:} ...'.format(sub_progress))

        line = line.strip()
        paper = json.loads(line)
        key_set = set(paper.keys())
        if  'lang' in key_set and paper['lang']=='en' and 'keywords' in key_set and 'fos' in key_set:
            # print paper['fos'],paper['keywords']
            ## 根据 fos 分别统计各个领域的关键词以及他们的词频
            fos = paper['fos']
            keywords = paper['keywords']
            for field in fos:
                for keyword in keywords:
                    field = field.lower()
                    keyword = keyword.lower()

                    fos_keyword_freq[field][keyword]+=1

    output_fos_keywords(fos_keyword_freq)

def output_fos_keywords(fos_keyword_freq):
    open('fos_keywords_freq.json','w').write(json.dumps(fos_keyword_freq))
    
    for field in fos_keyword_freq.keys():
        for keyword in fos_keyword_freq[field].keys():
            print field+'\t'+keyword+'\t'+str(fos_keyword_freq[field][keyword])


def extract_keywords_from_dir(dir_path):
    files = os.listdir(dir_path)
    progress = 0
    for single_file in files:
        progress+=1
        logging.info('Processing progress:{:}/{:} ... '.format(progress,len(files)))

        single_file_path = dir_path+'/'+single_file
        extract_keywords_from_single_file(single_file_path)



if __name__ == '__main__':
    # extract_keywords_from_single_file(sys.argv[1])
    extract_keywords_from_dir(sys.argv[1])
    # output_fos_keywords()