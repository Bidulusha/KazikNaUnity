import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    if n < 2:
        print(1)
        return

    max_val = max(arr)
    index_map = [0] * (max_val + 1)

    for i, num in enumerate(arr):
        index_map[num] = i + 1

    if index_map[1] > 0:
        for num in arr:
            if num != 1:
                print(f"{index_map[num]} {index_map[1]}")
                return

    processed = set()
    for num in sorted(arr):
        if num in processed:
            continue

        for divisor in range(1, int(num ** 0.5) + 1):
            if num % divisor == 0:
                if divisor in processed and divisor != num:
                    print(f"{index_map[num]} {index_map[divisor]}")
                    return
                other = num // divisor
                if other in processed and other != num:
                    print(f"{index_map[num]} {index_map[other]}")
                    return

        processed.add(num)

    print(1)

if __name__ == "__main__":
    main()
