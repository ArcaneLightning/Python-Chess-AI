# Python-Chess-AI
A chess AI made using python and the minimax algorithm (with alpha beta pruning)

The game is played in the terminal and is not a GUI

The user can play both <strong>WHITE</strong> and <strong>BLACK</strong>

The python chess library is NOT used

# Sample Output
<img src="./Chess Pic Starting.PNG" alt="Start position">
<img src="./Chess Pic 1st Move.PNG" alt="First Move by user">
<img src="./Chess Pic AI.PNG" alt="Second Move by AI">

## Getting started
Download the repository and install the numpy dependency (not very necessary to the code, so you could edit yourself and replace numpy arrays with lists):
```
git clone git@github.com:ArcaneLightning/Python-Chess-AI.git
cd Python-Chess-AI
pip3 install numpy
```

Run the program and start playing chess! ♟️
```
python3 main.py
```

### Example Moves
Moves should have the following format: (StartingSquare EndingSqare):
```
E2 E4
```
or
```
e2 e4
```
This will move the piece at e2 to e4.
