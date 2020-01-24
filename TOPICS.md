# Related topics

## MyPy
### Types:
To use types, you should add this syntax in your code
- define variable: `a:int=2`
- define function: `def test(a:int,b:int)->str:`

### check Type:
To check type of variables & input/output functions. run this command

`mypy filename.py`
in this case, the above code returs:
```
me.py:13: error: Argument 1 to "convert" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```
### type pros:
- Easy to documenting. Also there are a lot of module exist that auto generate documents from typed style code in python.
This advantage has been used in distrubuted languages such as GoLang,Rust to auto-generate documentation from strict type.
- Improve IDEs & linters to create structure of your code to hint some efficient suggestions and refactors.
### type cons:
- It takes times to add types.
- To work well with types, you should upgrade to newer python versions.
- Because of import typing module, the start-up time increases significant times

### .gitignore
All the items in .gitignore is choosed from **ref02**:
- _\_\_pycache\_\_/_ for python cache file
- _.idea_ for jetbrains config for project
- _env_ or _venv_ for virtual environment
- _.mypy_cache_ for mypy cache that created during the command `mypy`

## References:
1. https://realpython.com/python-type-checking/
2. https://github.com/github/gitignore/blob/master/Python.gitignore
3. https://www.python.org/dev/peps/pep-0484/#which-brackets-for-generic-type-parameters
4. https://www.python.org/dev/peps/pep-0526/#preferred-coding-style-for-variable-annotations
5. https://pep8.org/
6. https://www.python.org/dev/peps/pep-0257/

