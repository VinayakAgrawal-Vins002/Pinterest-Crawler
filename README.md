# Pinterest Crawler Script

<img src="https://raw.githubusercontent.com/SajjadAemmi/Pinterest-Crawler/main/Pinterest-Logo.png" width="400px">

Download Images from Pinterest using keywords in a Script rather than Manually using the Command Prompt Everytime.

## Usage

### CLI

Pinterest Crawler may be used directly in the Command Line Interface (CLI):

```bash
pinterest-crawler --keywords lion tiger bear
```

Also you can write your favorite keywords in a file for example `my_keywords.txt` and set path of file in `--keywords` argument:

```bash
pinterest-crawler --keywords my_keywords.txt
```

### Python

Pinterest Crawler may also be used directly in a Python environment, and accepts the same arguments as in the CLI example above:

```python
from pinterest_crawler import PinterestCrawler


pinterest_crawler = PinterestCrawler()
pinterest_crawler(keywords=['lion', 'programmer'])
```

<!-- Due to some limitations of Pinterest, you can download 100 images per keyword. If you want to download more images, you can run following command for infinite execution:

```
python loop.py
``` -->

## TODO
- [ ] download images in a loop
- [ ] download images in a specific size
- [ ] download images in a specific format
