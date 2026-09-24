'''urllib ke important submodules:
urllib
│
├── urllib.parse
├── urllib.request
├── urllib.error
└── urllib.robotparser
'''

from urllib.parse import urlparse
url="www.flipkart.com"
result=urlparse(url)
print(result)
'''ParseResult(scheme='', netloc='', path='www.flipkart.com', params='', query='', fragment='')
https://www.example.com/products?id=10
│       │               │       │
│       │               │       └── query
│       │               └────────── path
│       └────────────────────────── netloc
└────────────────────────────────── scheme
'''
print(type(result))

from urllib.parse import urljoin
print(urljoin("https://example.com/","about"))

from urllib.parse import quote
print(quote("hello world"))   #encode


from urllib.parse import unquote
print(unquote("hello world")) #decode