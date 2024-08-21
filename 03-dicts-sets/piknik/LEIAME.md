# Contador de piquenique

`piknik.py` faz o papel de um amigo contador em um piquenique:
registra as contribuições das pessoas, totaliza, e determina
os valores a pagar ou receber para cada pessoa.

```python3
>>> from piknik import main
>>> main('Ana 33 Bia 27 Caio 21.5 Dito 0'.split())
    4 participantes.
    Total de contribuições:   81.50
    Contribuição ideal:       20.38
    Ana	 33.00   receber  12.62
    Bia	 27.00   receber   6.62
    Caio	 21.50   receber   1.12
    Dito	  0.00     pagar  20.38

```