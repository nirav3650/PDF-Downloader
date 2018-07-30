# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:27:12 2018

@author: NIRAV.KAKKAD
"""

import urllib.request
import os
from bs4 import BeautifulSoup


class Pdfdownloader:

    def __init__(self):
        print("Download Pdf from website Pdf")

    def downloadpdf(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        for htmltag in soup.findAll('a', href=True):
            if os.path.splitext(os.path.basename(htmltag['href']))[1] == '.pdf':
                outputfile = os.path.basename(htmltag['href'])
                current = urllib.request.urlopen(htmltag['href'])
                print("\n Downloading: %s" % (outputfile))
                with open(outputfile, 'wb') as f1:
                    f1.write(current.read())
                print("Downloading Completed")


if __name__ == "__main__":

    obj = Pdfdownloader()
    website = input('Enter the url containing pdf: ')
    obj.downloadpdf(website)

