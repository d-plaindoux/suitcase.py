suitcase.py
===========

Simple and convenient python library dedicated to Pattern Matching 

Quick Overview
--------------

If you  want  to  manipulate object  based  on  types  in Python   the
dedicated design  pattern is the visitor.   Unfortunately even if such
pattern is well known its implementation is  always painful because it
implies code dissemination.

In  addition such mechanism only enables  selection based on types and
does not provides  a simple and  intuitive mechanism filtering objects
using their values i.e. attributes.

For  this   purpose   a simple  pattern    matching  inspired by Scala
[extractor  object](http://www.scala-lang.org/node/112)   has     been
designed.

### Simple example

Then pattern  matching cases can be done  on the object  kind and it's
internal state. For instance the following sample checks if an integer
is <tt>O</tt> or not.

``` python
from smallibs.suitcase.cases import _
from smallibs.suitcase.match import Match

isZero = Match.match();

isZero.caseOf(0).then(True);
isZero.caseOf(_).then(False);

isZero.match(0); # == True
```

### Recursive structural induction

Computation based on structural induction can be recursive.

``` python
from smallibs.suitcase.cases import var, reentrant
from smallibs.suitcase.cases.list import *
from smallibs.suitcase.match import Match

adder = Match.create()
adder.caseOf(Empty).then(0)
adder.caseOf(Cons(var,var.of(adder))).then(lambda i:i[0] + i[1])

adder.match([1,2,3]) # == 6 (A perfect number)
``` 

#### Rentrant recursive structural induction

Computation based on structural induction can also been provided using
`reentrant` capability for example.

``` python
from smallibs.suitcase.cases import var, reentrant
from smallibs.suitcase.cases.list import *
from smallibs.suitcase.match import Match

adder = reentrant(Match.create())
adder.caseOf(Empty).then(0)
adder.caseOf(Cons(var,var.of(adder))).then(lambda i:i[0] + i[1])

adder.match([1,2,3]) # == 6 (A perfect number)
``` 

