def cipher(string: str):
    """
    与えられた文字列の各文字を，以下の仕様で変換する関数
    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    word = [chr(219 - ord(i)) if i.islower() else i for i in string]

    return "".join(word)

message = 'the quick brown fox jumps over the lazy dog'
message = cipher(message)

print('暗号化:', message)
message = cipher(message)
print('復号化:', message)