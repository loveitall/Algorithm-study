## 나는 요리사다 문제

#  첫번째 풀이 방법
# score = []

# for i in range(5):
#     score.append(sum(map(int, input().split())))

# print(score.index(max(score))+1, max(score))


# 2번째 풀이 방법
# 이건 좀 더 생각 흐름대로 짠 부분
maxScore= 0
maxIndex = 0

for i in range(5):
    s1, s2, s3, s4 = map(int, input().split())
    score = s1 + s2 + s3 + s4
    if maxScore < score :
        maxScore = score
        maxIndex = i + 1

print(maxIndex, maxScore)

# 결과 실행창
# 5 4 4 5
# 5 4 4 4
# 5 5 4 4
# 5 5 5 4
# 4 4 4 5
# 4 19


