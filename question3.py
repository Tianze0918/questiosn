def main_num(num, listsum):
    return (listsum+num-1)//num

def median(num, list):
    return list[num//2]

def max_sum_subarray(arr, k):
    max_result = 0
    for start in range(len(arr) - k + 1):
        subarr = arr[start:start + k]
        subarr_sum = sum(subarr)
        subarr_median = median(k, subarr)
        temp_result = (subarr_sum+k-1)//k - subarr_median
        max_result = max(max_result, temp_result)
    
    return max_result

def maxval(sequence):
    result=0
    if len(sequence) < 2:
        return 0 
    sorted_seq=sorted(sequence)
    window=2
    while (window<=len(sequence)):
        temp_result=max_sum_subarray(sorted_seq,window)
        if temp_result>result:
            result=temp_result
        window+=1
    return result


def run():
    sequence = [1, 3, 9]
    print(maxval(sequence))

if __name__ == "__main__":
    run()