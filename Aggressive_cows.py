def can_we_place(stalls, distance, cows):
    n = len(stalls)
    cnt_cows = 1
    last = stalls[0]

    for i in range(n):
        if stalls[i] - last >= distance:
            cnt_cows += 1
            last = stalls[i]
        
        if cnt_cows >= cows:
            return True
    
    return False


def aggressive_cows(stalls, k):
    stalls.sort()
    n = len(stalls)
    low, high = 1, stalls[-1] - stalls[0]

    while low <= high:
        mid = (low + high) // 2
        
        if can_we_place(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    
    return high
