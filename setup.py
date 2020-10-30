import setuptools
from Cython.Build import cythonize

test = setuptools.Extension(
    name="pupil_av.test",
    sources=["src/pupil_av/test.pyx"],
    include_dirs=[],
)

setuptools.setup(ext_modules=cythonize([test]))
