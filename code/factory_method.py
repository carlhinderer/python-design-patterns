import json
import xml.etree.ElementTree as etree


class JsonDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XmlDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JsonDataExtractor
    elif filepath.endswith('xml'):
        extractor = XmlDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    process_json_file()
    process_xml_file()
    process_sqlite_file()


def process_json_file():
    print('Processing json file:\n')
    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()


def process_xml_file():
    print('Processing xml file:\n')
    xml_factory = extract_data_from('data/people.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} people')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text) 
        for p in liar.find('phoneNumbers')]
        print()


def process_sqlite_file():
    # Trying to process other file types raises exception
    print('Processing sqlite file:\n')
    sqllite_factory = extract_data_from('person.sq3')


main()