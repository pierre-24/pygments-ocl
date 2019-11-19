import pygments_ocl
from setuptools import setup
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

pkgs = []
dependency_links = []
for pkg in parse_requirements('requirements.txt', session=False):
    if pkg.link:
        dependency_links.append(str(pkg.link))
    else:
        pkgs.append(str(pkg.req))

setup(
    name=pygments_ocl.__name__,
    packages=['pygments_ocl'],
    version=pygments_ocl.__version__,
    author=pygments_ocl.__author__,
    author_email=pygments_ocl.__email__,
    description=pygments_ocl.__doc__,
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    install_requires=pkgs,
    entry_points='''[pygments.lexers]
                    ocl=pygments_ocl:OCLLexer''',
)
