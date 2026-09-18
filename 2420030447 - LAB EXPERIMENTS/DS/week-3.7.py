def h_dist(str1,str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be equal length")
    return sum(ch1 != ch2 for ch1,ch2 in zip(str1,str2))
s1="karolina"
s2="kathrin"
dist=h_dist(s1,s2)
print(f"Hamming distance between '{s1}' and '{s2}': {dist}")