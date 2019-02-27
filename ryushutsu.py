#!/bin/env python
from bs4 import BeautifulSoup
import itertools


def get_kanji_list(soup):
    table = soup.find('table', {'class': 'sortable wikitable'})
    rows = table.find('tbody').find_all('tr')
    return [cells[1].text[:1] for cells in [row.find_all('td') for row in rows] if len(cells) > 0]


def generate_gengo_list(kanji_list):
    return [x + y for (x, y) in itertools.product(kanji_list, kanji_list)]


def main():
    with open('joyo-kanji.html', 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        kanji_list = get_kanji_list(soup)
        for gengo in generate_gengo_list(kanji_list):
            print(gengo)


if __name__ == '__main__':
    main()
