import jieba.posseg as psg

def count(list):
    word_frequency={}
    for word in list:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
    word_sort=sorted(word_frequency.items(),key=lambda x:x[1],reverse=True )
    # 返回一个数组
    return word_sort


with open('1.txt','r',encoding='utf-8') as f:
    content=f.read()
    f.close()

lst_words=[]
for x in psg.cut(content):
    # 保留名词 人名 地名 长度至少两位
    if x.flag in ['n','nr','ns'] and len(x.word)>1:
        lst_words.append(x.word)

word_sort=count(lst_words)

print('\n序号\t名词\t词频\n')
for i in range(3):
    print('{}\t{}\t{}\n'.format(i+1,word_sort[i][0],word_sort[i][1]))