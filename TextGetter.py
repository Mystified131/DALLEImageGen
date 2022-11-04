
import requests
from bs4 import BeautifulSoup
import re
import enchant
from RandFunct import random_number
from RandFunct2 import random_number2

d = enchant.Dict("en_US")
    
def GetWebText():

    print("")

    print("Processing page.")

    print("")

    #sites = ['https://en.wikipedia.org/wiki/Science_Fiction', 'https://en.wikipedia.org/wiki/Mass_Effect']

    #sites = ['https://en.wikipedia.org/wiki/Modern_Art', 'https://en.wikipedia.org/wiki/Ancient_Art', 'https://en.wikipedia.org/wiki/Renaissance_Art']

    #sites = ['https://www.moma.org/learn/moma_learning/glossary/']

    sites = ['https://en.wikipedia.org/wiki/List_of_modern_artists', 'https://en.wikipedia.org/wiki/Lists_of_painters', 'https://en.wikipedia.org/wiki/List_of_contemporary_artists', 'https://en.wikipedia.org/wiki/List_of_sculptors', 'https://en.wikipedia.org/wiki/List_of_graphic_designers', 'https://en.wikipedia.org/wiki/List_of_illustrators', 'https://en.wikipedia.org/wiki/List_of_colors_by_shade#Colors_with_shades_and_tints_of_that_hue', 'https://en.wikipedia.org/wiki/List_of_two-dimensional_geometric_shapes' ]

    ln = len(sites)

    totstr = ""

    for str in range(ln):

        url = sites[str]

        xstr = requests.get(url).text

        totstr += xstr

    ylst = totstr.split(' ')

    xlst = []

    remword = ['asbox', 'parser', 'saved', 'idplogo', 'logged', 'inlili', 'alilia', 'page', 'hosted', 'a', 'pdf', 'cache', 'key', 'IP', 'main', 'portal', 'address', 'liliia', 'classnew', 'idpviews', 'content', 'titleHOW', 'article', 'articles', 'revision', 'Wikipedia', 'version', 'vector-menu', 'vector-menu-portal', 'Commons', 'registered', 'trademark', 'media', 'pages', 'Serialized', 'timestamp', 'vector-user-menu-legacy', 'non-profit', 'report', 'links', 'files', 'terms', 'edited']

    for elemi in ylst:
        elemj = elemi.lower()
        elem = elemj.strip()
        elem = elem.replace('-', '')
        elem = elem.replace('.', '')
        try:
            if (d.check(elem)) and (elem not in remword) and (not elem.isnumeric()) and (len(elem) > 4) and (elem not in xlst): 
                xlst.append(elem)
        except:
            print("Bad Char")

    print(xlst)

    return(xlst)