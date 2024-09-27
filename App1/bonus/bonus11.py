def get_average():
    with open("files/data.txt", 'r') as file:
        #这里读的是一个list
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)
