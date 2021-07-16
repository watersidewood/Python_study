with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.split(": ")

        eng_ans = data[0]
        kor_mean = data[1]

        eng_vocb = input("{}: ".format(kor_mean))

        if eng_ans == eng_vocb:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {} 입니다.".format(eng_ans))