# --- DEMO: Core types & literals ---
x = 42                 # int
y = 3.14               # float
z = "hello"            # str
t = True               # bool
lst = [[1, 2, 3, ["Arif", "Rahul", 3.5, 100*2], 4], [10 , 20, 30]]
ls2D =[ [1, 2, 3],[4, 5, 6] ]     # list (mutable)
tpl = (1, 2, 3, [1, 2, 3], "Arif")        # tuple (immutable)
dct = {"a": 1, "b": 2, "a": 3} # dict (mapping)
st = {1, 2, 2, 3, "Arif"}      # set (unique)
lst.append(10)

print(dct)
print(ls2D)
print(tpl)
print(st)
print(type(x), type(y), type(z), type(lst), type(tpl), type(dct), type(st))