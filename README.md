# Pygments OCL

A pygments plugin for OCL ([Object Constraint Language](https://en.wikipedia.org/wiki/Object_Constraint_Language)).
Packaged from [the work](https://github.com/soundasleep/iaml/tree/master/org.openiaml.docs.tools/latex/pygments-ocl) of @soundasleep.

To **install** it, just use pip:

```bash
pip3 install git+ssh://git@github.com:pierre-24/pygments-ocl.git
```

Then, `ocl` should appear as a lexer:

```text
$ pygmentize -L lexers | grep -i "ocl"
* ocl:
    OCL (filenames *.ocl)
```

To **use** it, just use the "ocl" language.