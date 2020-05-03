def punct(pop_list, lower=True):
    '''
    去除标点并让所有字母小写
    :param pop_list:所要处理的的列表格式
    :param lower:是否转小写，默认是
    :return all_comment:处理后的结果-字符串格式
    '''
    if not isinstance(pop_list, list):raise ValueError('pop_list is list')
    if not isinstance(lower, bool):raise ValueError('lower is bool')
    if len(pop_list) == 0: raise IOError('The list is empty')
    all_comment = ' '.join(pop_list)
    import re
    pattern = r'[^\w\s]'
    replace = ''
    all_comment = re.sub(pattern,replace,all_comment)
    if lower:
        all_comment = all_comment.lower()
    return all_comment
def statistics(pop_list, symbol = True, lower = True):
    '''
    词频统计
    :param pop_list:所要处理的的列表格式
    :param symbol:是否去除标点，默认是
    :param lower:是否转小写，默认是
    :return wordCount_dict:统计结果-字典格式
    '''
    if not isinstance(pop_list, list):raise ValueError('pop_list is list')
    if not isinstance(symbol, bool):raise ValueError('symbol is bool')
    if not isinstance(lower, bool):raise ValueError('lower is bool')
    if symbol:
        all_comment = punct(pop_list, lower)
    else:
        if len(pop_list) == 0: raise IOError('The list is empty')
        if lower:
            all_comment = ' '.join(pop_list).lower()
        else:
            all_comment = ' '.join(pop_list)
    from collections import Counter
    word_list = all_comment.split(' ')
    wordCount_dict = Counter(word_list)
    return wordCount_dict
def stop_words(statis, pop_list=[], symbol = True, lower=True, wordCount_dict={}):
    '''
    删除词频统计中的停顿词
    :param statis:是否选择词频清理
    :param pop_list:所要处理的的列表格式
    :param symbol:是否去除标点，默认是
    :param lower:是否转小写，默认是
    :param wordCount_dict:词频统计结果-字典
    :return wordCount_dict:清除后结果-字典格式
    '''
    if not isinstance(statis, bool):raise ValueError('statis is bool')
    if not isinstance(pop_list, list):raise ValueError('pop_list is list')
    if not isinstance(symbol, bool):raise ValueError('symbol is bool')
    if not isinstance(lower, bool):raise ValueError('lower is bool')
    if not isinstance(wordCount_dict, dict):raise ValueError('wordCount_dict is dictionary')
    if statis:
        if len(pop_list) == 0: raise IOError('The list is empty')
        wordCount_dict = statistics(pop_list, symbol, lower)
    with open("stopwords.txt") as file:
        stopword_list = [k.strip() for k in file.readlines()]
    for stopword in stopword_list:
        if stopword in wordCount_dict:
            wordCount_dict.pop(stopword)
    wordCount_dict.pop('')
    return wordCount_dict
def Count_Sort(wordCount_dict, choices_number = 0):
    '''
    字典排名数目排序
    :param wordCount_dict:词频统计结果-字典
    :param choices_number:返回前choices_number个字典个数
    :return keyword_list:出现的单词-列表格式
    :return value_list:单词对应的词频-列表格式
    '''
    if not isinstance(wordCount_dict, dict):raise ValueError('wordCount_dict is dictionary')
    if not isinstance(choices_number, int):raise ValueError('choices_number is number')
    count_list = sorted(wordCount_dict.items(), key=lambda x:x[1],reverse=True)
    if choices_number != 0:
        count_list = count_list[:choices_number]
    keyword_list = [k[0] for k in count_list]
    value_list = [k[1] for k in count_list]
    return keyword_list, value_list
def word_all(pop_list, choices_number = 0, symbol = True, lower=True):
    '''
    调用全部函数
    :param pop_list:所要处理的的列表格式
    :param choices_number:返回前choices_number个字典个数
    :param symbol:是否去除标点，默认是
    :param lower:是否转小写，默认是
    :return keyword_list:出现的单词-列表格式
    :return value_list:单词对应的词频-列表格式
    '''
    wordCount_dict = stop_words(True,pop_list,symbol,lower)
    keyword_list, value_list = Count_Sort(wordCount_dict, choices_number)
    return keyword_list, value_list