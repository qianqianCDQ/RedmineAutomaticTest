import csv


def parse_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for line in data:
            mylist.append(line)
        del mylist[0]
        return mylist


if __name__ == "__main__":
    data = parse_csv("../Data/test_01_login.csv")
    print(data)