# Pinterest Image Scraper

Now you can take the URL to any Pinterest board (or a CSV of a bunch of boards) and return a Python list of the URLs to the hi-rez versions of all of the images on the board.

## Requirements:

- Python 2.7
- Pandas (pip install pandas)
- Selenium (pip install selenium)
- A [Pinterest](http://www.pinterest.com) Account

## How to Run:

```
git clone https://github.com/xjdeng/pinterest-image-scraper.git
cd pinterest-image-scraper
import scraper as s
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>)
images = s.runme("http://URL-to-image-board")
```

### Or if you have a CSV file with a URL to a different image board on every line:

```
images = s.runme(imageboards.csv)
```

