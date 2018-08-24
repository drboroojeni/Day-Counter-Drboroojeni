#calculate the number of days between two dates
#checking whether year n is a leap year
def isLeap(n):
    m = n % 400
    if n%4 == 0 and m != 100 and m != 200 and m != 300:
        return True
#counting the number of days from date m1/d1/y1 to date m2/d2/y2. Returns zero if dates are equal, negative if second date is earlier than the first one, and positive otherwise.
# running time: O(1)
def dayCount(m1,d1,y1,m2,d2,y2): #recursively defined...
    dy = abs(y2-y1)
    if dy >= 400:#if the dates are more than 400 years apart...
        if y1 > y2:
            return dayCount(m1, d1, y2 + dy % 400, m2, d2, y2) - (365 * 400 + 97) * int(dy / 400)# in every 400 years, there are 97 leap years
        else:
            return dayCount(m1, d1, y1, m2, d2, y1 + dy % 400) + (365 * 400 + 97) * int(dy / 400)
    sum = 0
    if y1 < y2:
        for i in range(y1,y2):
            if isLeap(i):
                sum += 366
            else:
                sum += 365
        return dayCount(m1, d1, y2, m2, d2, y2) + sum
    if y2 < y1:
        return -dayCount(m2, d2, y2, m1, d1, y1)
    #runs the following code if only if y1 == y2
    if m1 < m2:
        for i in range(m1,m2):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12: # six months have 31 days
                sum += 31
            elif i == 2:
                if isLeap(y1):
                    sum += 29 # February of a leap year has 29 days...
                else:
                    sum += 28 # February of a non-leap year has only 28 days...
            else:
                sum += 30
        return dayCount(m2,d1,y1,m2,d2,y2)+sum
    if m1 > m2:
        return -dayCount(m2,d2,y2,m1,d1,y1)
    #continues the following code if and only if y1 == y2 and m1 == m2
    return d2-d1
print dayCount(6,1,2018,1,6,20018)
