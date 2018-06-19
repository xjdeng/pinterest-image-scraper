# Pinterest Image Scraper

Now you can take the URL to any Pinterest board (or a CSV of a bunch of boards) and return a Python list of the URLs to the hi-rez versions of all of the images on the board.

## Requirements:

- Python 2.7 or 3.5+ ([Anaconda](https://anaconda.org) recommended)
- Pandas (pip install pandas or conda install pandas)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) + [Gecko driver](https://github.com/mozilla/geckodriver/releases) (Firefox can be omitted if you know what you're doing and have another browser set up to be used via Selenium)
- Selenium (pip install selenium or conda install -c conda-forge selenium, then see [these instructions](https://pypi.python.org/pypi/selenium/3.9.0) for installing the Gecko driver)
- A [Pinterest](http://www.pinterest.com) Account

## How to Run:

```
git clone https://github.com/xjdeng/pinterest-image-scraper.git
cd pinterest-image-scraper
pip install -U .
cd ..
python
import scraper as s
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>)
images = ph.runme("http://URL-to-image-board")
```

### Or if you have a CSV file with a URL to a different image board on every line:

```
images = ph.getURLs(imageboards.csv)
```

### Now if you want to download these images:

```
s.download(images, "/path/to/your/destination/dir")
```

### or to download to your current directory:

```
s.download(images)
```

Note: you no longer need Firefox.  If you'd like to use a different browser (i.e. Chrome or PhantomJS), you'll need to initialize it through selenium, then pass it through the Pinterest_Helper object.  For example, using Chrome:

```
from selenium import webdriver
chrome = webdriver.Chrome()
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>, browser)
```

