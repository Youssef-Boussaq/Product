import re
text = "P1 est un produit composé de P2 et P3 \nP2 est un produit élémentaire \nP5 est un produit composé de P1 et P4 \nP4 est un produit élémentaire \nP9 est un produit composé de P1 , P6 et P4 \nP10 est un produit composé de P3 et P5 \nP11 est un produit composé de P5 et P3 "


x= re.findall(r"(P\d +est un produit élémentaire)",text)
print(*x,sep="\n")


t=re.findall(r"(P\d+ est un produit composé de P\d , P\d et P\d)",text)
print(*t,sep="\n")


y=re.findall(r"(P\d+ est un produit composé de P3 et P5)",text)
y+= re.findall(r"(P\d+ est un produit composé de P5 et P3)",text)
print(*y,sep="\n")

print("#"*40)
r = re.findall(r"(P\d+ est un produit composé+) de P[^2]", text)
for i in r:
    print(i)
print("#"*40)

pattern = r"(P\d+ est un produit composé de P1 , P6 et P4 )"
matches = re.findall(pattern, text)

print(matches)



