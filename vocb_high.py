import random

vocb_dic = {}

with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.split(": ")
        eng_ans = data[0]
        kor_mean = data[1]
        vocb_dic[eng_ans] = kor_mean

keys = list(vocb_dic.keys())

while True:
    index = random.randint(0, len(keys) - 1)
    eng_answ = keys[index]

    kor_means = vocb_dic[eng_answ]

    eng_vocb = input("{}: ".format(kor_means))
    if eng_vocb == 'q':
        break
    elif eng_answ == eng_vocb:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 {} 입니다.".format(eng_answ))