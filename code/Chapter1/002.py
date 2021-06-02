# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
string_1 = 'パトカー'
string_2 = 'タクシー'
ans = ''
for i in range(4):
    ans += string_1[i] + string_2[i]

print(ans)

"""
# answer
str1 = 'パトカー'
str2 = 'タクシー'
ans = ''.join([i + j for i, j in zip(str1, str2)])

print(ans)
"""