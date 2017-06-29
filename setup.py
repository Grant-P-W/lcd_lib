# Workaround for issue in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'lcdlib',
      version           = '1.5.1',
      author            = 'Grant Wodny',
      author_email      = 'trduunze@gmail.com',
      description       = 'Library to control a 16x2 lcd screen',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/Grant-P-W/',
      dependency_links  = ['https://github.com/Grant-P-W/lcd_lib/'],
      install_requires  = [''],
      packages          = find_packages())
