input_ = [2, 7, 11, 15, 3, 19, -2, 0, 145]
target = 19

num2idx = dict(zip(input_, range(len(input_))))
for num in num2idx.keys():
    try:
        if num2idx[num] < num2idx[target - num]:
            print (num2idx[num] + 1, num2idx[target - num] + 1)
        else:
            print (num2idx[target - num] + 1, num2idx[num] + 1)
        break
    except KeyError:
        continue
