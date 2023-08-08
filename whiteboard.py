# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]					
# Example Output: [11,2,3,4,0,0]

def solution(li): # O(n)
    count = 0 # O(1)
    new_li = [] # O(1)
    for i in range(len(li)): # O(n)
        if li[i] == 0:
            count += 1 # O(1)
        else:
            new_li.append(li[i]) # O(1)
    while count > 0:
        new_li.append(0) # O(1)
        count -= 1 # O(1)
    return new_li # O(1)


# remove all zeroes and count
# add the amount of zeros in count

# print(solution([0,1,0,3,12]))