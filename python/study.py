import random

def selection_sort(data) :
    for i in range(len(data) -1) :
        min_index = i
        for j in range(i + 1, len(data)) :
            if data[j] < data[min_index] :
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    

data = random.sample(range(100), 5)
selection_sort(data)
print(data)




