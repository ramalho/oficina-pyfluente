# Classe Vector

  **DICA**: execute estes testes com

Representa um vetor Euclideano bidimensional: um objeto com atributos `x` e `y`.

```python
>>> from vector2d import Vector
>>> v1 = Vector(2, 4)
>>> v1.x
2
>>> v1.y
3

```

Objetos `Vector` implementam alguns operadores aritméticos:

Adição:

```python
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 6)

```

Comprimento do vetor, também conhecido como módulo, norma ou valor absoluto:

```python
>>> v = Vector(3, 4)
>>> abs(v)
5.0

```

Multiplicação escalar:

```python
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0

```
