def main_num(num, listsum):
    return (listsum+num-1)//num

def median(num, list):
    return list[num//2]

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(1, len(arr)-k+1):
        window_sum = window_sum - arr[i-1] + arr[i+k-1]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def maxval(sequence):
    result=0
    if len(sequence) < 2:
        return 0 
    tmain=0
    tmedian=0
    sorted_seq=sorted(sequence)
    window=2
    while (window<=len(sequence)):
        tmain=main(window, max_sum_subarray(sorted_seq,window))
        tmedian=median(window, sorted_seq)
        temp_result=tmain-tmedian
        if temp_result>result:
            result=temp_result
        window+=1
    return result


