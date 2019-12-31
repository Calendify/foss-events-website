import csv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from helper import generate_event_details_path
from parser import parse_events

# this script generates the event detail pages

file_loader = FileSystemLoader('src/templates')
env = Environment(loader=file_loader)
template = env.get_template('event.html')


def generate_event_pages(events, year):
    for event in events:
        result = template.render(
            event=event,
        )

        filepath = generate_event_details_path(event)
        with open('build/' + filepath, 'w') as f:
            f.write(result)


today = datetime.now()

for year in [2019, 2020]:
    with open('data/' + str(year) + '_events_db.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        events = parse_events(reader, today)
        generate_event_pages(events['all'], year)
