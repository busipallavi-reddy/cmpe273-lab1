# cmpe273-lab1


Implemented external sorting in the following manner:

* Sorted each individual file using in-built python library and wrote it to temporary sorted files.
* Used min heap to merge elements from each of the temporary sorted files and continued the merge process(heapify) till all the elements were sorted and written to a single output file.

Time observation without using asycio -

time python3 ext_merge_sort.py 

real	0m0.073s
user	0m0.053s
sys	0m0.020s

As for asyncio external sort, implemented the above algorithm by converting the i/o and merge functions as async.

Time ovservation with asyncio -

time python3 async_ext_merge_sort.py 

real	0m0.091s
user	0m0.079s
sys	0m0.012s

As the input was small and CPU has more power, the time taken by asyncio was a little larger than normal external sort. When I tried with 10 files with 10,000 numbers each or more number of files, asyncio performed much better than the sync program.
