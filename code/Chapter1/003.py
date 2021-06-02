import re
string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

ans = re.sub('[,\.]', '', string).split()
print(*[len(i) for i in ans])

"""
# answer
import re

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = re.sub('[,\.]', '', str)  # ,と.を除去
splits = str.split()  # スペースで区切って単語ごとのリストを作成
ans = [len(i) for i in splits]

print(ans)
"""