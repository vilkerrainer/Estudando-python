if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    n1 = list(set(arr))

    n1.sort(reverse=True)
    
    n2 = n1[1]
    
    print(n2)