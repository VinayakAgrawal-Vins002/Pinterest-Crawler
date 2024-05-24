# Pinterest Crawler Script

<img src="https://github.com/VinayakAgrawal-Vins002/Pinterest-Crawler/blob/main/Pinterest-Logo.png" width="400px">

Download Images from Pinterest using keywords Defined in a Simple Script rather than Manually using the Command Prompt Everytime, or Making Changes in the Crawler Function which I believe to be Harder for Beginners in Coding Like Me. The Crawler Script Gives Access to a small amount of Customization For Better Organisatation.

It can Loop over Multiple Search Strings, with an approximate amount of images to download per individual search (if you want to limit the download) and later onn Organise the images in Named Folders as and when the entire Search has been downloaded. 

## Usage

### CLI

Pinterest Crawler may be used directly in the Command Line Interface (CLI):

```python
pinterest-crawler --keywords AI Art Animated
```

Also you can write your favorite keywords in a file for example `my_keywords.txt` and set path of file in `--keywords` argument.

```python
pinterest-crawler --keywords my_keywords.txt
```

### Python Script

Pinterest Crawler may also be used directly in the Python Script named Crawler, for easier use by Begineers follow the Below Steps:

```python
1. 'pip install pinterest-crawler' Through the Terminal
2. Clone or Download the Crawler.py File 
3. Make appropriate Changes as per your requirements in the File as prompted by the Comments [Search Strings, Download Paths, Counts, etc]
4. Run The Script 'python -u "path\to\the\file\Crawler.py"'
```

## Issues
- [ ] I Did Notice some Issue with my Download Loop, which either Tends To Terminate Too Early or Keeps Downloading Even After Reaching the Count and Therefore Has To Be Terminated Manually From The Terminal using 'Ctrl + C' sometimes.

## Notes
- [ ] This is my First Repository Fork, please forgive me if I may have made any issues in the Crawler Script or mistakes while Forking as this was just a Learning Experiance For me, and Vist the Main Branch By @Sajjad Aemmi For More Clarification on the Main Crawler. Thank you for your understanding.
- [ ] I plan on using the Downloaded Images with  the AutoChange Wallpaper App For Changing Images From Everytime I unlock my Phone - wanting to Have a variety of Images Suitable as Wallpapers and neatly Organised at the same time in different sub-folders based on their topics just in case I ever need to access them.
- [ ] This was the Motivaion For writing an Automation Script - Rather than doing this downloadig process manually For each search term I wanted a Script that I could use To Automate the Downloading while I would sit back and relax.
- [ ] Will add the Repo Link Here if Someone wants to access my Filtered Images or use the same For themselves with the Wallpaper App.
