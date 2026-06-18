if __name__ == '__main__':
    K = int(input())
    n = list(map(int, input().split()))
    d = {}
    for i in n:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, value in d.items():
        if value == 1:
            print(key)
