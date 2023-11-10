import re

test_str = """
            aaaabd asdfas/ asdfasdf
            asdfasd.asdfa MBSD{ここだ}
            MBSD{ここだよん}MBBSSD{}M}adfad/ad/
            """
test_str2 = 'aaaMBSD{XXXX}bbb'
# 正規表現パターン
pattern = r'(?<=MBSD\{).*(?=\})'
# 正規表現でマッチング

print(re.findall(r'(?<=MBSD\{)[0-9 a-z A-Z]*(?=})', test_str))
print(re.findall(r'(?<=MBSD\{)[^\}]+(?=\})', test_str))