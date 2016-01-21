nums1 = [1, 3, 6, 8, 10, 10, 10]
nums2 = [-100, 0, 4, 10, 101]

m = n = 0
len1 = len(nums1)
len2 = len(nums2)
result = []
while m < len1 or n < len2:
    if nums1[m] <= nums2[n]:
        result.append(nums1[m])
        if m == len1 - 1:
            if n == len2 - 1:
                result.append(nums2[n])
                break
            else:
                n += 1
        else:
            m += 1
    else:
        result.append(nums2[n])
        if n == len2 - 1:
            if m == len1 - 1:
                result.append(nums1[m])
                break
            else:
                m += 1
        else:
            n += 1

median = result[len(result) / 2]
print result, median

