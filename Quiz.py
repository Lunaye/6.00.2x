def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    l = []
    first = songs[0]
    space = max_size
    
    if first[2] > max_size:
        return l
    else:
        l.append(first[0])
        space -= first[2]
        del songs[0]        

    sizes = {}
    for i in songs:
        sizes[i[0]] = i[2]
    sorted_songs = sorted(sizes, key=sizes.get)    
    for s in sorted_songs:
        if sizes[s] <= space:
            l.append(s)
            space -= sizes[s]
    return l

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = 0
    for num in L:        
        (quot, rem) = divmod(s,num)
        multipliers += quot
        s = rem
    return multipliers if s == 0 else 'no solution'

def max_contig_sum(L):
    
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L
    """
    length = len(L)
    sums = []       
    for i in range(lengtg):
        for j in range(i,length):
            sums.append(sum(L[i:j+1]))
               
    return max(sums)
