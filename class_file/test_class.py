import re

test_str = "https://animestore.docomo.ne.jp/animestore/tp_pc"
domain   = "animestore.docomo.ne.jp"
print(test_str[:8+len(domain)])