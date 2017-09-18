from setuptools import setup

setup(name='searchscrapeserver',
      version='0.1',
      description='Server implementation scraping a number of popular servers',
      url='https://github.com/EdmundMartin/SearchScraperAPI',
      author='Edmund Martin',
      author_email='edmartin101@googlemail.com',
      license='GPL-3.0',
      packages=['searchscrapeserver'],
      install_requires=[
      	'aiohttp',
      	'lxml',
      	'bs4',
      	'marshmallow',
      ],
      zip_safe=False)