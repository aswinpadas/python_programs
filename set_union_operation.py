# Hacker Rank Sets : Set .union() Operation solution
if __name__ == '__main__':
    n = int(input())
    first_news_sub = set(map(int, input().split()))
    n = int(input())
    second_news_sub = set(map(int, input().split()))
    print(len(first_news_sub.union(second_news_sub)))
