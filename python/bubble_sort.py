#오른쪽 값과 비교해 더 작은 값 앞으로 보내기

def bubble_sort(data) :
    for i in range (len(data)-1) :

        for j in range(len(data)-1-i) :

            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
            print(j, j+1)

data = [2,3,1,5,4,9,7,8,11,31,20,29]
bubble_sort(data)
print(data)
