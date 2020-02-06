import heapq

def read_from_file(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def write_to_temp_files(filename, list):
    with open(filename, "w") as f:
        for val in list:
            f.write(str(val) + "\n")

def write_to_file(value):
    with open("output/sorted.txt", "a") as f:
        f.write(str(value) + "\n")

def mergesort(nums):
    l = len(nums)
    if l > 1:
        mid = l//2
        L = nums[:mid]
        R = nums[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

def sort_file(i):
    filename = "input/unsorted_" + str(i + 1) + ".txt"
    nums = read_from_file(filename)
    # nums.sort()
    mergesort(nums)
    write_to_temp_files("output/sorted_" + str(i + 1) + ".txt", nums)

def merge():
    file_handlers = []

    for i in range(10):
        file_handlers.append(open("output/sorted_"+str(i+1)+".txt", "r"))

    heap = [(int(file_handlers[file].readline().strip()), file) for file in range(len(file_handlers))]
    heapq.heapify(heap)

    while heap:

        smallest, file = heapq.heappop(heap)

        write_to_file(smallest)

        value = file_handlers[file].readline()
        if value:
            heapq.heappush(heap, (int(value.strip()), file))

def main():

    for i in range(10):
        sort_file(i)

    merge()

if __name__ == "__main__":
    main()