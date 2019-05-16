#DayDayUpQ1.py


'''
#DayDayUpQ4.py
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayf = 0.001
while dayup(dayf) < 37.87:
    dayf += 0.001
print("工作日努力的参数{:.3f}".format(dayf))
'''
