assert 1 == 1  # Check 1

assert 1 == 1  # Check 2

"""
Multiline comment before statement is ok
"""
assert 1 == 1  # Check 3

# Comment before statement
assert 1 == 1  # Check 4

if 1 == 1:  # Check 5
    assert 1 == 1
elif 2 == 2:
    assert 1 == 1
else:
    assert 1 == 1

for a in [1, 2]:  # Check 6
    assert 1 == 1
else:
    assert 1 == 1

while 1 < 2:  # Check 7
    assert 1 == 1
else:
    assert 1 == 1

try: # Check 8
    assert 1 == 1
except Exception:
    assert 1 == 1
