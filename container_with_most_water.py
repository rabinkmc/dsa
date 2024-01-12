# https://leetcode.com/problems/container-with-most-water/

def container_with_most_water(heights):
    i = 0 
    j = len(heights) - 1
    max_area = 0 
    while ( i < j ):
        area = min(heights[i], heights[j]) * ( j - i) 
        if area > max_area:
            max_area = area

        if (heights[i] < heights[j]):
            i = i + 1
        else:
            j = j - 1

    return max_area

heights = [1,8,6,2,5,4,8,3,7]

print(container_with_most_water(heights))
