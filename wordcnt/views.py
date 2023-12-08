from collections import Counter

from django.shortcuts import render

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create your views here.
def word_cnt_form(request):
    return render(request, "wordcnt/wordcntForm.html")


def word_cnt_process(request):
    wordv = request.POST['wordv']
    wordv = wordv.replace('\r\n', ' ')
    wordv = wordv.split(' ')
    stop_word = ['', '있습니다', '수', '것입니다.', '더', '여러분', '등', '위해', '더욱'
                 ,'있는','매','나가겠습니다.','저는','속에서','있고', '그리고', '합니다. ', '이', '아니라', '하는', '지금']
    wordv_total = []
    for tag in wordv:
        if tag not in stop_word:
            wordv_total.append(tag)
    print('*' * 30)
    word_cnt = Counter(wordv_total)
    # most_common() : 빈도수가 높은 순으로 집계
    print(word_cnt.most_common(20))
    word_cnt_totalList = word_cnt.most_common(20)

    font_location = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
    wordcloudv = WordCloud(font_path=font_location, background_color='white',max_words=50,relative_scaling=0.3,width=800,height=450)\
        .generate_from_frequencies(word_cnt)
    plt.figure(figsize=(15,10))
    plt.imshow(wordcloudv)
    plt.axis('off')
    plt.savefig('/home/ict01/PycharmProjects/demo/main/static/wordcntImg/wordcnt.png')
    return render(request, 'wordcnt/wordcntProcess.html',{'wordv_cnt_totalList':word_cnt_totalList})