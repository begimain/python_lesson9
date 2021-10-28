# a = [1, 2, 3, 4, 5]
# b = 0
#
# for i in a:
#     pass
#     b = b + i
#     print(b)
def bank(a, years):
    i = 0
    while i < years:
        a = a + a*0.1
        i = i + 1
        return a





if __name__ == '__main__':
    print(bank(1000, 5))





