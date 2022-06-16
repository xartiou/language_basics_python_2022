"""
result = (условие) ? выражение:1 выражение:2

(a - b) if a > b else 1 / 0
"""

num = input("Enter a number:")
print("Это число" if num.isdigit() else "Это  не число")
