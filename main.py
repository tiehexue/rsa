import rsa
from padding import chunk_string
from padding import padding

m_length = len(str(rsa.m)) - 1
unicode_size = 7

info = '''央视网消息（新闻30分）：烈士纪念日向人民英雄敬献花篮仪式30日上午在北京天安门广场隆重举行。
          党和国家领导人习近平、李克强、栗战书、汪洋、王沪宁、赵乐际、韩正、王岐山等，同各界代表一起出席仪式。'''
print(info)

unicode = [padding(ord(c), unicode_size) for c in info]
print(unicode)

# string to numbers
encoded = ''.join(unicode)
print(encoded)

integers = chunk_string(encoded, m_length)
print(integers)

secrets = rsa.encode(list(map(lambda x: int(x), integers)))
print(''.join([str(i) for i in secrets]))

decoded_integers = rsa.decode(secrets)
last = decoded_integers[-1]
del decoded_integers[-1]
decoded = [padding(i, m_length) for i in decoded_integers]
decoded.append(str(last))
print(decoded)

chunks = chunk_string(''.join(decoded), unicode_size)
print(''.join([chr(int(d)) for d in chunks]))
