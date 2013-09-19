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

Then pattern  matching cases can be done  on the object  kind and it's
internal state. For instance the following sample checks if an integer
is <tt>O</tt> or not.

``` python
from smallibs.suitcase.cases.core import _
from smallibs.suitcase.match.matcher import Match

isZero = Match.match();

isZero.caseOf(0).then(True);
isZero.caseOf(_).then(False);

isZero.match(0); # == True
```
