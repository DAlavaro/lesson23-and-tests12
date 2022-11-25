from collections import Counter


def top3(input_str):
    c = Counter(input_str)
    return [item[0] for item in c.most_common(3)]


if __name__ == "__main__":
    print(top3('11111111222222223333333344444444555555'))