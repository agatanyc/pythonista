from bs4 import BeautifulSoup
import urllib.request

prettify = BeautifulSoup.prettify

def slurp(fname):
    """(str) -> str

    Returns the text of the named file or url.
    """
    if "://" in fname:
        with urllib.request.urlopen(fname) as input:
            return input.read().decode('utf-8')
    else:
        with open(fname) as input:
            return input.read()

def find_batch(soup, batch_id):
    tags = soup.select('ul#batch' + str(batch_id))
    if tags:
        return tags[0]

def person_name(person):
    '''(Tag) -> str'''
    return person.select('div.name')[0]('a')[0].get_text()


if __name__ == '__main__':
    # file = 'https://www.hackerschool.com/private'
    file = 'hs-private.html'
    html = slurp(file)
    soup = BeautifulSoup(html)
    batch = find_batch(soup, 16)    # Batch 16 is Winter 1, 2014.

    format = '{:32} {}'

    print()
    print(format.format('Name', 'Pythonista?'))
    print(format.format('----', '-----------'))
    for person in batch.select('li.person'):
        pythonista = 'yes' if 'python' in person.get_text().lower() else 'no'
        print(format.format(person_name(person), pythonista))
    print()

    # Prettify converts soup to a string.

