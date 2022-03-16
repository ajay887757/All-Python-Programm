d={'A':100,'Z':200,'B':300}
# 1st items  2nd items 3rd items
for k,v in d.items():
    print(k,v)
print("Sorted")
for k,v in sorted(d.items()):
    print(k,v)
