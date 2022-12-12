
def lab2_1_10 (data):
    answer_string = ""
    for value in data:
        answer_string = answer_string + chr(int(value,16))
    return answer_string

answer = lab2_1_10(['49', '74', '73', '20', '6a', '75', '73', '74', '20', '61', '20', '66', '6c', '65', '73', '68', '20', '77', '6f', '75', '6e', '64'])