
# Pertinencia
a = {1, 2, 3, 4}
print('O numero 9 pertence  a A?',9 in a)
print('O numero 1 pertence  a A?',1 in a)



# Continencia
a = {1, 2, 3, 4}
b = {1, 2, 3, 4, 5, 6, 7}
c = a.intersection(b)
if a == c:
    print("O conjunto A está contido em B")
else:
    print("O conjunto A não está contido em B")

# Subconjunto
a = {1, 2, 3, 4, 5}
c = {1, 2, 3, 4}
print('O conjunto C é Subconjunto de A? ', c.issubset(a))


# Igualdade
a = {4, 2, 3, 1, 8}
c = {4, 3, 1, 2, 8}
if a == c:
    print("Igual")
else:
    print("Não igual")
