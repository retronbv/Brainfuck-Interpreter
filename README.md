# Brainfuck Interpreter
A Brainfuck interpreter!

```shell
$ pip install brainf_interpret
```
Then use it in your files!
```python3
import brainf_interpret as bf
bf.run(">>>+>")
```
**OR**
```python3
import brainf_interpret as bf
with open("./brainfuck.txt") as file:
  bf.run(file.read())
```