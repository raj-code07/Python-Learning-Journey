# Write a program to count frequency of each character
#  in the string "banana" using a dictionary.

# text ="banana"
# freq={}

# for ch in text:
#     freq[ch]=freq.get(ch,0)+1

# print(freq)


text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1  # agar pehle se hai to count badhao
    else:
        freq[ch] = 1   # agar pehli baar mila to 1 se shuru karo

print(freq)