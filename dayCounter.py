#calculate the number of days between two dates

def isLeap(n):
    m = n % 400
    if n%4 == 0 and m != 100 and m != 200 and m != 300:
        return True

def dayCount(m1,d1,y1,m2,d2,y2):
    dy = abs(y2-y1)
    if dy >= 400:
        if y1 > y2:
            return dayCount(m1, d1, y2 + dy % 400, m2, d2, y2)-97*dy/400-365*dy
        else:
            return dayCount(m1, d1, y1, m2, d2, y1 + dy % 400)+97*dy/400+365*dy
    sum = 0
    if y1 < y2:
        for i in range(y1,y2):
            if isLeap(i):
                sum += 366
            else:
                sum += 365
        return dayCount(m1,d1,y2,m2,d2,y2)+sum
    if y2 < y1:
        return -dayCount(m2,d2,y2,m1,d1,y1)
    if m1 < m2:
        for i in range(m1,m2):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                sum += 31
            elif i == 2:
                if isLeap(y1):
                    sum += 29
                else:
                    sum += 28
            else:
                sum += 30
        return dayCount(m2,d1,y1,m2,d2,y2)+sum
    if m1 > m2:
        return -dayCount(m2,d2,y2,m1,d1,y1)
    return d2-d1
print ((-500)/400, dayCount(1,1,2018,1,1,18))