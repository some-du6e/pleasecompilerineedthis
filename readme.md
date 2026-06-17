<h1>PCINT</h1>
honestly not even a compiler

## Installation
first install it from pip
```bash
pip install pleasecompilerineedthis
```

and then just run it
```bash
python -m pleasecompilerineedthis
```

## Usage
Running just it alone brings you to a python style repl
```bash
python -m pleasecompilerineedthis
```

You can add --help to see all options
```bash
python -m pleasecompilerineedthis --help
```

To compile:
```bash
python -m pleasecompilerineedthis -c INPUT.pls -o OUTPUT.py
```



## Example
```python
plz name = ask("Name please: ")
log("Hello, " + name + "!")
```
or view [example.pls](./example.pls)

## Reference

| name | description | python counterpart | example|
|------|-------------|--------------------|--------|
| `plz`  |defines a variable| [nothing] | `plz result = 1 + 1`
| `log`  |prints something | `print` | `log("result", result)`
| `ask` | asks for input | `input` | `input("Your name: ")`
| `anderdingus` | mention him anywhere for good luck | [nothing] | `log("please anderdingus")`

