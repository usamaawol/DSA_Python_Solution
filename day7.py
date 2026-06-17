def split_and_join(line):
    days = line.split(" ")
    result = "-".join(days)
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
