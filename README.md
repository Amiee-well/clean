## 数据清洗--cleancc

---

### cleancc
- 快速清洗数据内容可以
- 项目地址(欢迎star):[https://github.com/Amiee-well/cureUi](https://github.com/Amiee-well/cureUi)

### 使用方法
- pip install cleancc

- import cleancc

- 共有五个函数调用：

  1.第一个函数为punct：

  ​	去除标点并让所有字母小写
​    :param pop_list:所要处理的的列表格式
  ​    :param lower:是否转小写，默认是
​    :return all_comment:处理后的结果-字符串格式
  
2.第二个函数为statistics：
  
​	词频统计
  ​    :param pop_list:所要处理的的列表格式
​    :param symbol:是否去除标点，默认是
  ​    :param lower:是否转小写，默认是
​    :return wordCount_dict:统计结果-字典格式
  
  3.第三个函数为stop_words：
  
  ​	删除词频统计中的停顿词
  ​    :param statis:是否选择词频清理
  ​    :param pop_list:所要处理的的列表格式
  ​    :param symbol:是否去除标点，默认是
  ​    :param lower:是否转小写，默认是
  ​    :param wordCount_dict:词频统计结果-字典
  ​    :return wordCount_dict:清除后结果-字典格式
  
  3.第四个函数为Count_Sort：
  
  ​	字典排名数目排序
  ​    :param wordCount_dict:词频统计结果-字典
  ​    :param choices_number:返回前choices_number个字典个数
  ​    :return keyword_list:出现的单词-列表格式
  ​    :return value_list:单词对应的词频-列表格式
  
  4.第五个函数为word_all：
  
  ​	调用全部函数
  ​    :param pop_list:所要处理的的列表格式
  ​    :param choices_number:返回前choices_number个字典个数
  ​    :param symbol:是否去除标点，默认是
  ​    :param lower:是否转小写，默认是
  ​    :return keyword_list:出现的单词-列表格式
  ​    :return value_list:单词对应的词频-列表格式

### 注意事项
- 注意:处理数据参数类型为列表，需要pandas转换为列表后进行调用！

- 使用示例:
    
    import pandas as pd
    from clean import word_all
    from bs4 import BeautifulSoup
    
    df = pd.read_csv("label.csv",sep='\t', escapechar='\\')
    review_list = df['review'].tolist()
    comment_list = [BeautifulSoup(k,'lxml').text for k in review_list]
    print(comment_list)
    
    keyword_list, value_list = word_all(comment_list,150)
    print(keyword_list, value_list)
