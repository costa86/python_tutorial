def count_binary_substrings(s):
    groups = []
    count = 1

    for i in range(1, len(s)):
        
        if s[i] == s[i - 1]:
            count += 1
            continue
        
        groups.append(count)
        count = 1
    
    groups.append(count)
    return groups

a = count_binary_substrings("00110")
print(a)