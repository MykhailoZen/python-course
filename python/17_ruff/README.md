N802 Function name `Add` should be lowercase
 --> messy.py:4:5
  |
4 | def Add(a, b):
  |     ^^^
5 |     result = a + b
6 |     unused = 42
  |

F841 Local variable `unused` is assigned to but never used
 --> messy.py:6:5
  |
4 | def Add(a, b):
5 |     result = a + b
6 |     unused = 42
  |     ^^^^^^
7 |     msg = "done"
8 |     return result
  |
help: Remove assignment to unused variable `unused`

F841 Local variable `msg` is assigned to but never used
 --> messy.py:7:5
  |
5 |     result = a + b
6 |     unused = 42
7 |     msg = "done"
  |     ^^^
8 |     return result
  |
help: Remove assignment to unused variable `msg`

E711 Comparison to `None` should be `cond is None`
  --> messy.py:12:13
   |
11 | def check(x):
12 |     if x == None:
   |             ^^^^
13 |         print("none!")
14 |     return x
   |
help: Replace with `cond is None`

Found 4 errors.
No fixes available (3 hidden fixes can be enabled with the `--unsafe-fixes` option).