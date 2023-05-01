# nsloader
This parser is a Python script that can collect articles from a news site by inputting its URL.

### Installing nkparser and Supported Versions
----------------------
nsloader is not registered on the pypi. You have to download from github directly.
```
$ python -m pip install git+https://github.com/new-village/nsloader.git
```
nsloader is tested by Python `3.10.4`.
  
  
### Dependencies
----------------------
- [requests](https://docs.python-requests.org/en/latest/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
- [selenium](https://www.selenium.dev/)
  
### Usage
----------------------
To load the [Wall Street Journal](https://www.wsj.com/) articles ~~and parse to dictionay file~~.

#### Wall Street Journal
```python
>>> from nsloader import wsj
>>> session = wsj.auth_session()
>>> response = session.get('https://www.wsj.com/articles/the-fed-...')
>>> print(BeautifulSoup(response.content, 'html.parser').title.text)
"The Fed Failed but Wants More Power - WSJ"
```