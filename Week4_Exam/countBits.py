import math
def countBits(num):

    if not num:
        return [0]
    if num == 1:
        return [0, 1]
    if num == 2:
        return [0, 1, 1]
    ans = [0] * (num + 1)
    ans[1] = 1
    cl = 1
    cr = int(math.log(num + 1, 2.0))
    l = 1
    while cl != cr:
        l = 2 * l
        for i in range(l, l + l / 2):
            ans[i] = ans[i - l / 2]
        for i in range(l + l / 2, 2 * l):
            ans[i] = ans[i - l / 2] + 1
        cl += 1
    l = 2 * l
    if num + 1 < l + l / 2: 
        for i in range(l, num + 1):
            ans[i] = ans[i - l / 2]
    else:
        for i in range(l, l + l / 2):
            ans[i] = ans[i - l / 2]
        for i in range(l + l / 2, num + 1):
            ans[i] = ans[i - l / 2] + 1
    return ans
    
solu = countBits(15)
# # solu = countBits(16)
# # solu = countBits(1)
# # solu = countBits(25)
# # solu = countBits(5)
# solu = countBits(6)
print(solu)
