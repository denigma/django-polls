from distutils.core import setup


setup(
    name='django-polls',
    version='0.4',
    packages=['polls'],
    package_data={'polls': ['templates/polls']},
    license='',
    long_description=open('README.rst').read(),
    url='http://www.denigma.de',
    author='Hevok',
    author_email='hevok@denigma.de'
)
