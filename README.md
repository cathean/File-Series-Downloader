# File Series Downloader

## Version 1.0.0
File Series Downloader - is simple download manager for serial files in the internet. You can use this sofware to download files with number name on it in one go.

## Usage
For example you want to download files with these urls :

```
https://cathean.com/data1.pdf
https://cathean.com/data2.pdf
https://cathean.com/data3.pdf
... And so on.
```
You can replace the number with `{{S}}` so it will become like this `https://cathean.com/data{{S}}.pdf` That's it. The rest is self-explained :)

## Known Limitations
* There's some minor bug.
* Can't download files with number over 100.
* Can't download files with multiple serial number.
* Has no pause nor stop feature.

## About
This program written in Python and powered by PyQt.
