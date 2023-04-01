def get_average():
    with open("file/files.txt", "r") as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        average = sum(values) / len(values)
        return average

    return data


average = get_average()
print(average)