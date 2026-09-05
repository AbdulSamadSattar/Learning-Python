# ---------- Christmas Tree (centered) ----------
n = 5
for i in range(1, n):
    print(" " * (n - i) + "* " * i)

print()

# ---------- Right Angle Triangle (inverted, left-aligned) ----------
rows = 4
for i in range(rows):
    print(" " * i + "*" * (rows - i))