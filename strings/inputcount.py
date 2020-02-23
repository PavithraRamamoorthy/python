def finddigits_charssymbols(inputstring):
  words = inputstring.split()
  print(words)
  char_count = 0
  digit_count = 0
  symbol_count = 0
  for char in inputstring:
   if char.islower() or char.isupper():
       char_count+=1
   elif char.isnumeric():
       digit_count+=1
   else:
       symbol_count+=1

  print("Chars = ", char_count, "Digits = ", digit_count, "Symbol = ", symbol_count)

inputstring = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols")
print(finddigits_charssymbols(inputstring))