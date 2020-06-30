"""
pygments-ocl: a pygments plugin for OCL (Object Constraint Language)
"""

__name__ = 'pygments-ocl'
__version__ = '0.1'
__author__ = 'Pierre Beaujean and Jevon Wright (soundasleep)'
__maintainer__ = 'Pierre Beaujean'
__email__ = 'pierre.beaujean@unamur.be'
__status__ = 'Development'

from pygments.lexer import RegexLexer, include, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation

__all__ = ['OCLLexer']


# adapted from https://github.com/soundasleep/iaml/blob/master/org.openiaml.docs.tools/latex/pygments-ocl/ocl.py
# based on PythonLexer
class OCLLexer(RegexLexer):
    """
    For OCL source code
    """

    name = 'OCL'
    aliases = ['ocl']
    filenames = ['*.ocl']
    mimetypes = ['text/x-ocl', 'application/x-ocl']

    _keywords = [
        'context',
        'inv',
        'pre',
        'post',
        'body',
        'def',
        'if',
        'then',
        'else',
        'library',
        'metamodel',
        'require',
        'public',
        'definitions',
        'init',
        'derive',
        'endif',
        'enddefinitions',
        'endlibrary',
        'let',
        'package',
        'endpackage',
        'static'
    ]

    _keywords_type = [
        'Sequence',
        'Set',
        'Bag',
        'OrderedSet',
        'Boolean',
        'Integer',
        'Real',
        'String',
        'Tuple',
        'OclAny',
        'Collection',
        'OclInvalid',
        'OclVoid',
        'OclMessage',
        'UnlimitedNatural'
    ]

    _functions = [
        'oclIsTypeOf',
        'oclIsKindOf',
        'oclIsUndefined',
        'oclIsInvalid',
        'oclAsType',
        'oclIsNew',
        'allInstances',
        'isUnique',
        'isEmpty',
        'includes',
        'excludes',
        'select',
        'collect',
        'exists',
        'forAll',
        'size',
        'sum',
        'product',
        'includes',
        'asSet',
        'asOrderedSet',
        'asBag',
        'asSequence',
        'one',
        'abs',
        'floor',
        'max',
        'min',
        'round',
        'div',
        'mod',
        'concat',
        'substring',
        'toInteger',
        'toLowerCase',
        'toReal',
        'toUpperCase',
        'indexOf',
        'union',
        'selectByKind',
        'any',
        'notEmpty',
        'oclIsInState',
        'reject',
        'closure',
        'includesAll',
        'iterate',
        'flatten',
        'collectNested',
        'count',
        'excludesAll',
        'oclType',
        'oclLocale',
        'toString',
        'equalsIgnoreCase',
        'at',
        'characters',
        'toBoolean',
        'selectByType',
        'intersection',
        'including',
        'excluding',
        'symmetricDifference',
        'append',
        'prepend',
        'insertAt',
        'subOrderedSet',
        'first',
        'last',
        'reverse',
        'subSequence',
        'sortedBy'
    ]

    _operator = [
        'in',
        'is',
        'and',
        'or',
        'xor',
        'not',
        'implies'
    ]

    tokens = {
        'root': [
            (r'\n', Text),
            (r'^(\s*)("""(?:.|\n)*?""")', bygroups(Text, String.Doc)),
            (r"^(\s*)('''(?:.|\n)*?''')", bygroups(Text, String.Doc)),
            (r'[^\S\n]+', Text),
            (r'#.*$', Comment),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'[]{}:(),;[]', Punctuation),
            (r'\\\n', Text),
            (r'\\', Text),
            (words(_operator, suffix=r'\b'), Operator.Word),
            (r'<>|!=|==|->|<<|>>|\?|[-~+/*%=<>&^|.!]', Operator),
            include('keywords'),
            include('builtins'),
            include('name'),
            (r'("(\\\\|\\"|[^"])*")|(\'(\\\\|\\\'|[^\'])*\')', String),
            include('numbers'),
        ],
        'keywords': [
            (words(_keywords, suffix=r'\b'), Keyword),
            (words(_keywords_type, suffix=r'\b'), Keyword.Type),
            (r'(true|false|null|invalid)\b', Keyword.Constant),
            (words(_functions, suffix=r'\b'), Keyword.Pseudo),
        ],
        'builtins': [
            (r'(self|none)\b', Name.Builtin),
        ],
        'numbers': [
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-f]+', Number.Hex),
            (r'[0-9]+L?', Number.Integer),
        ],
        'name': [
            (r'@[a-zA-Z0-9_.]+', Name.Decorator),
            ('([a-zA-Z$_]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD])' # Start character
             '([a-zA-Z$_]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|[\uF900-\uFDCF]|[\uFDF0-\uFFFD][0-9])*' # Continuation character
             , Name
             ),
        ],

}
