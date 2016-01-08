from spack import *

class PyScipy(Package):
    """Scientific Library for Python."""
    homepage = "https://pypi.python.org/pypi/scipy"
    url      = "https://pypi.python.org/packages/source/s/scipy/scipy-0.15.0.tar.gz"

    version('0.14.0','d7c7f4ccf8b07b08d6fe49d5cd51f85d',
           url='https://pypi.python.org/packages/source/s/scipy/scipy-0.14.0.tar.gz')
    version('0.15.0', '639112f077f0aeb6d80718dc5019dc7a')
    version('0.15.1', 'be56cd8e60591d6332aac792a5880110')

    extends('python')
    depends_on('py-nose')
    depends_on('py-numpy')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
