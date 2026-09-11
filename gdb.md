---

`int 3` is an instruction that is primarly used to by debuggers to put breakpoints.  
`run` is used for executing programs.
`continue` to resume the program's execution.
`info registers` allows viewing the state of registers on cpu.

--- 
`print` or `p` can be used to show results of expressions.  
It's syntax:
```bash
> p/f <expression>

f as a format can be:
  x -> hexadecimal
  f -> float
  d -> signed integers
  u -> unsigned integers
  o -> octals
  t -> binary
  a -> address
  c -> chars
  s -> strings
```
Example:
```bash
> p/d $rax+0x100  
```
`p &var` can be used to find the address and type of a variable.  

---
To inspect memory `x/nfu addr` is used.
Syntax:
```bash
> x/nfu $rax+8

x -> examine
n -> integer
f is a format specifier:
  s -> strings
  i -> to disassembly
  x -> hexadecimal 
  f -> floats
  d -> signed integers
u is a size specifier:
  b -> bytes
  h -> halfwords (2 bytes)
  w -> words (4 bytes)
  g -> giant words (8 bytes)
```
Example:
```bash
x/nfw $rbp-4
```
---
Breakpoints can be put manually. `break` or `b` command can be used to achieve it.  
Relatively simple syntax:
```bash
> b *address
> b function
```
---
Values can be changed with `set` command
```bash
> set {type}address = value
```

Example
```bash
> p &var
$1 = (unsigned long *) 0x404035 <var>

> set {unsigned long *}0x404035 = 0x4444444
```