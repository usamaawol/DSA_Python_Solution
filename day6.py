if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(row[1]), int(row[2]))
        elif command[0] == "print":
            print(lst)
        elif command0] == "remove":
            lst.remove(int(row[1]))
        elif command[0] == "append":
            lst.append(int(row[1]))
        elif cpmmand[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
        elif command[0] == "sort":
            lst.sort()
