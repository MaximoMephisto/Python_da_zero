import unicodedata

s = "giù"
x = unicodedata.normalize("NFD", s)

print(x)