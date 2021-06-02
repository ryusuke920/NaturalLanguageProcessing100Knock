string_1 = 'paraparaparadise'
string_2 = 'paragraph'

def bi_gram(n, word):
    return list(zip(*[word[i:] for i in range(n)]))

X = set(bi_gram(2, string_1))
Y = set(bi_gram(2, string_2))
union = X | Y
intersection = X & Y
difference = X - Y


print('X:', X)
print('Y:', Y)
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)
print('Xにseが含まれるか:', {('s', 'e')} <= X)
print('Yにseが含まれるか:', {('s', 'e')} <= Y)