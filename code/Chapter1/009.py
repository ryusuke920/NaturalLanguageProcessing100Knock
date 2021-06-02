import random
"""
# randomについて
・ランダムに要素を一つ選択: random.choice()
・ランダムに複数の要素を選択（重複なし）: random.sample()
・ランダムに複数の要素を選択（重複あり）: random.choices()
"""
def shuffle(words):
    result = []
    for word in words.split():
        if len(word) >= 5:
            word = word[0] + ''.join(random.sample(word[1:len(word) - 1], len(word) - 2)) + word[-1]
        result.append(word)
    
    return ' '.join(result)

words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = shuffle(words)

print(ans)