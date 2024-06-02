# 성적 입력
score = {'국어':0, '수학':0, '영어':0}
hab = 0
avg = 0

for i in score.keys():
    score[i] = int(input(f"{i} 점수를 입력하세요 :"))
    hab += score[i]
avg = hab / len(score)
score['총합'] = hab
score['평균'] = avg
print(score)
