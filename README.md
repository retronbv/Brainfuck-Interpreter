# Brainfuck Interpreter
A Brainfuck interpreter written in Python!

Made by **[Touchcreator](https://repl.it/@Touchcreator)**, **[retronbv](https://repl.it/@retronbv)** and **[thecoder876](https://repl.it/@thecoder876)**

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