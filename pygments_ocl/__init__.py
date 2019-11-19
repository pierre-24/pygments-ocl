"""
pygments-ocl: a pygments plugin for OCL (Object Constraint Language)
"""

__name__ = 'pygments-ocl'
__version__ = '0.1'
__author__ = 'Pierre Beaujean and Jevon Wright (soundasleep)'
__maintainer__ = 'Pierre Beaujean'
__email__ = 'pierre.beaujean@unamur.be'
__status__ = 'Development'

from pygments.lexer import RegexLexer, include, bygroups
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
        'implies',
        'endif',
        'enddefinitions',
        'endlibrary'
    ]

    _keywords_type = [
        'Sequence',
        'Set',
        'Bag',
        'OrderedSet',
        'Integer',
        'Boolean',
        'Real',
        'String'
    ]

    _functions = [
        'oclIsTypeOf',
        'oclIsKindOf',
        'oclAsType',
        'oclIsNew',
        'allInstances',
        'isUnique',
        'isEmpty',
        'includes',
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
            (r'(in|is|and|or|not)\b', Operator.Word),
            (r'<>|!=|==|->|<<|>>|[-~+/*%=<>&^|.!]', Operator),
            include('keywords'),
            include('builtins'),
            include('name'),
            (r'"(\\\\|\\"|[^"])*"', String),
            include('numbers'),
            (r'({})\b'.format(' | '.join(_functions)), Name.Function),
        ],
        'keywords': [
            (r'({})\b'.format(' | '.join(_keywords)), Keyword),
            (r'({})\b'.format(' | '.join(_keywords_type)), Keyword.Type),
            (r'(true|false|null)\b', Keyword.Constant),
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
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
        ],
    }
