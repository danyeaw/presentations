class: title

# Intro to Typing and MyPy

---

```python
TypeError: method() takes exactly 1 positional argument (2 given)
```

```python
TypeError: 'NoneType' object is not iterable in Python
```

```python
TypeError: sequence item 0: expected str instance, int found
```

```python
TypeError: unhashable type: 'list'
```

---

# All Programming Languages Have a Type System

- Define interfaces between different parts of a program, and then check that
  the types have been connected consistently
- Apply to various parts of the program: variables, expressions, functions, or
modules


---

# Python is Dynamically (and Strongly) Typed

- The Python interpreter does type checking only
as code is run
- You can modify the type of an object after it is created
- TypeErrors are throw if you try to do operations on incompatible types (also
called type safety)
  
```python
> 3 + 4 + "5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

---

# Static Typing

- Some languages like C and Java are statically typed
- Types are checked at compile time

---

# Weak Typing

- Some languages like Javascript are weakly typed
- Positive: could be less work to convert data
- Negative: potential bugs due to unexpected results

```javascript
> 3 + 4 + 5
12 
> 3 + 4 + "5"
"75"
```

---

# Duck Typing

- If it walks like a duck
- The appearance of compatibility is more important than the class of an object
  itself
  
```python
class Duck:
  def fly(self):
    print("Duck flying")

class Goose:
    def fly(self):
        print("Goose flying")
```

---

# PEP 484 - Type Hints

- Adds type hints for functions in Python in 3.5+
- Relies on other tools to check them, like mypy

---

# Without Annotations

```python
def greeting(name):
    return f"Hello {name}"
```

---

# With Annotations

```python
def greeting(name: str) -> str:
    return f"Hello {name}"
```
---

# PEP 526 - Variable Annotations

- Adds syntax for annotating variables to Python 3.6+

```python
age: int = 37
```
```python
old: bool
```

---

# PEP 585 - Built-in Collection Types

In Python 3.9+ you can now use collection types like `list` and `dict` directly
without importing `List` and `Dict` from the typing module.

---
class: title

# mypy demo

---

# Two or More Types

```python

from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
      return "user-{100000 + user_id}"
    else:
        return user_id
```
---

# Optional Types
```python
from typing import Optional

def greeting(name: Optional[str] = None) -> str:
    if name is None:
        name = "stranger"
    return f"Hello {name}"
```

---

# Type Inference

```python
from typing import Iterable

def nums_below(nums: Iterable[float], lim: float) -> list[float]:
    output = []
    for num in nums:
        if num < lim:
            output.append(num)
    return output
```

mypy infers output is of type `list[float]` and num is a `float`

---

# Type Checking of Classes
```python
class A:
    def __init__(self, x: int) -> None:
        self.x = x  # Aha, attribute 'x' of type 'int'

a = A(1)
a.x = 2  # OK!
a.y = 3  # Error: 'A' has no attribute 'y'
```

---

# Advantages

- Think through your code interfaces more as you write them
- Better documentation of your code for you and others
- Improved autocomplete and error detection in IDEs
- Type checkers help prevent bugs before they are introduced

---

# Gradual Adoption

Type hints can be added gradually

Go out there and start adding them to your code now!