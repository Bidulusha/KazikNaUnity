def main():
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr) if arr else 0
    present = [0] * (max_val + 1)

    for i in range(n):
        present[arr[i]] = i + 1

    for i in range(n):
        num = arr[i]
        multiple = num * 2
        while multiple <= max_val:
            if present[multiple] != 0:
                print(present[multiple], i + 1)
                return
            multiple += num

    print("0 0")


if __name__ == "__main__":
    main()
