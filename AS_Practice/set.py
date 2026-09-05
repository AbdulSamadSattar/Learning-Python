# ---------- Creating Sets ----------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
empty = set()

print("a:", a)
print("b:", b)

# ---------- Adding Elements ----------
a.add(10)              # add single element
a.update([20, 30])     # add multiple elements
print("after add/update:", a)

# ---------- Removing Elements ----------
a.remove(10)            # removes, error if not found
a.discard(100)           # removes, no error if not found
popped = a.pop()         # removes random element
print("after remove/discard/pop:", a, "| popped:", popped)

# a.clear()              # removes all elements (uncomment to test)
print("\n","\bSet Operations","\n")
# ---------- Set Operations ----------
print("Union:", a | b, "==", a.union(b))
print("Intersection:", a & b, "==", a.intersection(b))
print("Difference (a-b):", a - b, "==", a.difference(b))
print("Symmetric Diff:", a ^ b, "==", a.symmetric_difference(b))

# ---------- In-place Update Versions ----------
c = a.copy()
c.intersection_update(b)
print("intersection_update:", c)

c = a.copy()
c.difference_update(b)
print("difference_update:", c)

c = a.copy()
c.symmetric_difference_update(b)
print("symmetric_difference_update:", c)

c = a.copy()
c.update(b)
print("update (union in-place):", c)

# ---------- Comparison Functions ----------
x = {1, 2}
y = {1, 2, 3}
print("issubset:", x.issubset(y))
print("issuperset:", y.issuperset(x))
print("isdisjoint:", x.isdisjoint({9, 10}))

# ---------- Other Useful Functions ----------
print("length:", len(a))
print("max:", max(a))
print("min:", min(a))
print("sum:", sum(a))
print("sorted:", sorted(a))

# ---------- Membership Test ----------
print("2 in a:", 2 in a)
print("100 not in a:", 100 not in a)

# ---------- Copying ----------
d = a.copy()
print("copy:", d)

# ---------- Frozenset (immutable set) ----------
fs = frozenset([1, 2, 3])
print("frozenset:", fs)