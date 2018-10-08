import rsa
from padding import chunk_string
from padding import padding

m_length = len(str(rsa.m)) - 1
unicode_size = 7

info = '''爻((╬ಠิ益ಠิ))ｲｶﾘｽﾞﾑｯ!! 癶(癶;:゜;益;゜;)癶鼻子很搶戲～顏文字表情符號系列 (๑・ิ⋖⋗・ิ๑) (́◉◞౪◟◉‵) 
( ^ิ౪^ิ) (◞≼○≽◟◞౪◟◞≼○≽◟) （ ´☣///_ゝ///☣｀）'''

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
