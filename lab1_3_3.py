
def lab1_3_3 (data):
    length = len(data)
    middle = length // 2
    start = data[:middle][::-1]
    end = data[middle:]
    return start+end

answer = lab1_3_3("sandwich")