# The world's slowest UTF-8 decoder function

The `utf8` module is executable pseudocode to explain how the
UTF-8 encoding/decoding algorithm works.

It is a didactic example and never intended to be used in
production. 

The `utf.decode()` function uses pattern matching to make the
algorithm of UTF-8 decoding easy to understand. But it is a 
terrible example of pattern matching in practice
because expanding bits into lists of integers is extremely
ineficient.

Maybe one day Python can have a syntax for efficient pattern matching
of bit patterns, like Erlang has:

https://erlang.org/doc/programming_examples/bit_syntax.html

Meanwhile, this (mis)use of `match/case` to handle bit patterns
is very slow but still a good way to understand how UTF-8 works.
