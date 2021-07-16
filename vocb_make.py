with open('vocabulary.txt', 'w') as f:
    while True:
        eng_vocb = input("영어 단어를 입력하세요: ")
        if eng_vocb == "q" :
            break

        kor_mean = input("한국어 뜻을 입력하세요: ")
        if kor_mean == "q":
            break

        f.write("{}: {}\n".format(eng_vocb, kor_mean))