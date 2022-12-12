
def lab2_1_9 (data):
    answerlist = []
    for eachnum in range(1,1001):
        if eachnum % data == 0:
            answerlist.append(eachnum)
    return answerlist
answer = lab2_1_9(5)
