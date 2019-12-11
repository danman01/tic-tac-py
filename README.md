# Tic-Tac-Py

Command-line based tic-tac-toe

Use any tokens you like!

When running included tests, make sure to choose X and O for them to work correctly.

## What game play looks like:

```python
user:~/tic-tac (master)$ python
Python 3.7.4 (default, Jul  9 2019, 18:13:23)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import game
run game.new_game() to start
>>> game.new_game()
Player 1:X
Player 2:O
X, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]2,2
board is now
 [['' '' '']
 ['' '' '']
 ['' '' 'X']]
O, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]0,1
board is now
 [['' 'O' '']
 ['' '' '']
 ['' '' 'X']]
X, what space would you like? spaces available: [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]0,0
board is now
 [['X' 'O' '']
 ['' '' '']
 ['' '' 'X']]
O, what space would you like? spaces available: [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]0,2
board is now
 [['X' 'O' 'O']
 ['' '' '']
 ['' '' 'X']]
X, what space would you like? spaces available: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]1,1
board is now
 [['X' 'O' 'O']
 ['' 'X' '']
 ['' '' 'X']]
Winner! X won with [0, 4, 8]: [['X', 'O', 'O'], ['', 'X', ''], ['', '', 'X']]
run game.new_game() to restart
>>> game.new_game()
Player 1:poop
Player 2:pee
poop, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]2,2
board is now
 [['' '' '']
 ['' '' '']
 ['' '' 'poop']]
pee, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]2,1
board is now
 [['' '' '']
 ['' '' '']
 ['' 'pee' 'poop']]
poop, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]2,0
board is now
 [['' '' '']
 ['' '' '']
 ['poop' 'pee' 'poop']]
pee, what space would you like? spaces available: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]0,0
board is now
 [['pee' '' '']
 ['' '' '']
 ['poop' 'pee' 'poop']]
poop, what space would you like? spaces available: [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]1,2
board is now
 [['pee' '' '']
 ['' '' 'poop']
 ['poop' 'pee' 'poop']]
pee, what space would you like? spaces available: [(0, 1), (0, 2), (1, 0), (1, 1)]1,1
board is now
 [['pee' '' '']
 ['' 'pee' 'poop']
 ['poop' 'pee' 'poop']]
poop, what space would you like? spaces available: [(0, 1), (0, 2), (1, 0)]0,1
board is now
 [['pee' 'poop' '']
 ['' 'pee' 'poop']
 ['poop' 'pee' 'poop']]
pee, what space would you like? spaces available: [(0, 2), (1, 0)]1,0
board is now
 [['pee' 'poop' '']
 ['pee' 'pee' 'poop']
 ['poop' 'pee' 'poop']]
poop, what space would you like? spaces available: [(0, 2)]0,2
board is now
 [['pee' 'poop' 'poop']
 ['pee' 'pee' 'poop']
 ['poop' 'pee' 'poop']]
Winner! poop won with [2, 5, 8]: [['pee', 'poop', 'poop'], ['pee', 'pee', 'poop'], ['poop', 'pee', 'poop']]
run game.new_game() to restart
>>> exit()
```
