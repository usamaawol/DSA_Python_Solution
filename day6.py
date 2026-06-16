if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        row = input().split()
        if row[0] == "insert":
            lst.insert(int(row[1]), int(row[2]))
        elif row[0] == "print":
            print(lst)
        elif row[0] == "remove":
            lst.remove(int(row[1]))
        elif row[0] == "append":
            lst.append(int(row[1]))
        elif row[0] == "pop":
            lst.pop()
        elif row[0] == "reverse":
            lst.reverse()
        elif row[0] == "sort":
            lst.sort()
