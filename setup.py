from setuptools import setup

version = '0.2'

setup(
    name='bonito',
    version=version,
    description="Generate a print & cut numerated tickets in PDF from a SVG template",
    author='Martín Gaitán',
    author_email='gaitan@gmail.com',
    url='http://mgaitan.github.io/posts/bonito-feito-pero-efectivo/',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=True,
    install_requires=['docopt'],
    py_modules=['bonito'],
    entry_points={
        'console_scripts': ['bonito=bonito:main'],
    },
)