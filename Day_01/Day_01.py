a=45
print(type(a))

a="İbrahim ALTIKAT"
print(type(a))

a=4.5
print(type(a))

Output
<class 'int'>
<class 'str'>
<class 'float'>

#--------------------------------------------------------------------------------------------------------------

a="Python İle Fonksiyonel Programlama"
print(dir(a))

Output
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#--------------------------------------------------------------------------------------------------------------

a="String ifade"
print(help(a.swapcase))

#Output
#Help on built-in function swapcase:

#swapcase() method of builtins.str instance
#    Convert uppercase characters to lowercase and lowercase characters to uppercase.