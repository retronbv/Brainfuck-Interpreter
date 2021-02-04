# Brainfuck-Interpreter
A Brainfuck interpreter!

```python3
import brainf_interpret as bf
bf.run(">>>+>")
```
**OR**
```python3
import brainf_interpret as bf
with open("./oof.bf") as file:
  bf.run(file.read())
```