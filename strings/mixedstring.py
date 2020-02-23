def mix_string(s1, s2):
  s2 = s2[::-1]
  length_s1 = len(s1)
  length_s2 = len(s2)
  length = length_s1 if length_s1 > length_s2 else length_s2
  result_string=""
  for i in range(length):
    if(i < length_s1):
        result_string = result_string + s1[i]
    if(i < length_s2):
        result_string = result_string + s2[i]
        print(result_string)
s1 = "Pynative"
s2 = "Website"
mix_string(s1, s2)