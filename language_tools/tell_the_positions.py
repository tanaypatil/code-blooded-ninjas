
def main():
    t = int(input())
    data = []
    for i in range(t):
        name, s1, s2, s3 = input().split()
        s1, s2, s3 = int(s1), int(s2), int(s3)
        entry = {
            "name": name,
            "total": s1 + s2 + s3
        }
        data.append(entry)
    data = sorted(data, key=lambda x: x['total'], reverse=True)
    for index,value in enumerate(data,1):
        print(index, value["name"])



if __name__ == "__main__":
    main()