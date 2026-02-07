def secret_cipher(s, cipher):
    result = []
    for char in s:
        result.append(cipher.get(char, "?"))
    return "".join(result)
print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'