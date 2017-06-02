# pypi-info-retriever
Retrieves package summary and licensing information from pypi repository

## Prerequisities
requests: `pip install requests`

## Usage
A semicolon separated list of module;version is read from the standard input,
a CSV with name, version, license_info, summary, homepage information is written to the standard output

##### Sample input:
~~~~
celery;4.0.2
requests;2.14.2
multiprocessing;2.6.2.1
scipy;0.18.1
~~~~
##### Sample output:

~~~~
"name","version","license","summary","homepage"
"celery","4.0.2","BSD","Distributed Task Queue.","http://celeryproject.org"
"requests","2.14.2","Apache 2.0","Python HTTP for Humans.","http://python-requests.org"
"multiprocessing","2.6.2.1","BSD Licence","Backport of the multiprocessing package to Python 2.4 and 2.5","http://code.google.com/p/python-multiprocessing"
"scipy","0.18.1","BSD","SciPy: Scientific Library for Python","https://www.scipy.org"
~~~~