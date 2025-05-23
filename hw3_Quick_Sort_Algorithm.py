# -*- coding: utf-8 -*-
"""作業3 - 快速排序演算法實作

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lGpT-IS_fAvv-5GWe2ogsJsZwNOmBApE
"""

def QuickSort(array, start, end):
    # Base case: if the sub-array has one or zero elements, it's already sorted
    if start >= end:
        return

    # 選擇當前子陣列的第一個元素作為 pivot
    pivot = array[start]
    left = start + 1
    right = end
    print("Choosing pivot", pivot, "at index", start)

    # Partitioning
    while left <= right:
        while left <= right and left < len(array) and array[left] <= pivot:
            left += 1
        while left <= right and right >= 0 and array[right] > pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
            print("  Swapped ->", array)

    # 確保 right 沒有超出邊界後再放置 pivot
    if start < len(array) and right < len(array):
        array[start], array[right] = array[right], array[start]
        print("Placed pivot", pivot, "at index", right, ":", array)
        print()

        # 分別遞迴處理左右子陣列，新的 recursive call 會有自己的 pivot
        QuickSort(array, start, right - 1)
        QuickSort(array, right + 1, end)


def main():
    # 讀取使用者輸入
    input_str = input("請輸入數字，以逗號分隔: ")
    input_parts = input_str.split(",")
    array = []
    for part in input_parts:
        part = part.strip()
        if part != "":
            array.append(int(part))

    if len(array) == 0:
        print("請輸入至少一個數字。")
        return

    print("原始陣列:", array)
    print()
    QuickSort(array, 0, len(array) - 1)
    print("排序後的陣列:", array)

if __name__ == "__main__":
    main()