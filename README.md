# nsloader  
[![Test](https://github.com/new-village/nsloader/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/new-village/nsloader/actions/workflows/unittest.yaml)  
This script collects articles from [Wall Street Journal](https://www.wsj.com/) and returns it in dict format.  
  
### Installing nsloader and Supported Versions
----------------------
nsloader is not registered on the pypi. You have to download from github directly.
```
$ python -m pip install git+https://github.com/new-village/nsloader.git
```
nsloader is tested by Python `3.10.4`.
  
  
### Dependencies
----------------------
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
- [selenium](https://www.selenium.dev/)
  
### Usage
----------------------
To load the [Wall Street Journal](https://www.wsj.com/) articles and parse to dictionay format.

#### Wall Street Journal  
NOTE: You have to set 2 enviroment valiables name as `WSJ_USERNAME` and `WSJ_PASSWORD` before execution.

```python
>>> from nsloader import wsj
>>> article = wsj.Article()
>>> article.load('https://www.wsj.com/articles/...')
>>> print(article.to_dict())
{"url": "https://www.wsj.com/articles/...", "title": "The Fed ...", "sub_title": "As expected ...",  ... }
```
