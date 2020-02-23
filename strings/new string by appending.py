def append_middle(s1, s2):
    middle_index = int(len(s1) /2)
    print("Original Strings are", s1, s2)
    middle_three = s1[:middle_index-1:]+ s2 +s1[middle_index-1:]
    print("After appending new string in middle", middle_three)
append_middle("pavithra", "pavithraramamoorthy")