## 나는 요리사다 문제
score = []

for i in range(5):
    score.append(sum(map(int, input().split())))

print(score.index(max(score))+1, max(score))

# 결과 실행창
# 5 4 4 5
# 5 4 4 4
# 5 5 4 4
# 5 5 5 4
# 4 4 4 5
# 4 19