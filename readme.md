Multi Site Image Grabber  
========================

A python script with (planned) support for batch downloading files and images from most popular hosts, social media sites, chans and others.

Currently supports:
-------------------
  * PrimeJailbait
  * 4chan

Instructions:
-------------
Setup.py just installs BeautifulSoup (required)
If you don't have that, or don't know what it is, open cmd and run:

    cd Drive:\folder\wherever\You\Extracted\The\Zip\file
    setupy.py install
    
Once that's done, run the script using the syntax:

    msig.py examplesite.com/this/is/an/example.html Drive:\Wherever\You\Want\To\Save\The\Images

So something like:

    msig.py http://boards.4chan.org/wg/res/5480554 G:\Pictures\4chan\Wallpapers\hidden profanities\

Planned things:
---------------

Support incoming for:  
  * DeviantArt (Galleries [Galleries initially, pages/profiles later])
  * Tumblr
  * Pinterest
  * Facebook (Galleries [Galleries initially, pages/profiles later])
  * Reddit (I'm not familiar with reddits api, so support will be bad initially)  

Things I might do if I get bored:
  * Add a GUI

Suggestions for other sites to support are welcome, but keep in mind this is intended as a batch downloader.



