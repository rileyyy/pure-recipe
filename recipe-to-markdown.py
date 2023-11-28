from recipe_scrapers import scrape_me
from rich.console import Console 
import sys
import argparse
import yaml

recipe_url = sys.argv[1]

console = Console()

scraper = scrape_me(recipe_url)


def format_file_name(recipe_title):
    """
    Converts the ls

    :param recipe_title: a string containing a recipe title.
    :return: formatted title
    :rtype: string
    """
    s = list(recipe_title.lower())

    for i, char in enumerate(s):
        if char.isspace():
            s[i] = '-'
    return "".join(s)


def save_to_markdown():

    title = scraper.title()
    recipe_file = format_file_name(title) + '.md'

    # TODO: if recipe file exists, make copy with -1 extension?

    with open(recipe_file, "w") as text_file:
        print(f"# {title}", file=text_file)
        print(f"**Serves:** {scraper.yields()}", file=text_file)
        print(f"**Total Time:** {scraper.total_time()} mins", file=text_file)
        print(f"\n## Ingredients", file=text_file)
        for ingredient in scraper.ingredients():
            print(f'-', ingredient, file=text_file)
        print(f"\n## Instructions", file=text_file)
        for index, instruction in enumerate(scraper.instructions_list()):
            print(f'{index+1}.', instruction, file=text_file)

def view_in_terminal():
    """
    
    :param url: a url string from a recipe website
    :return: 
    :rtype:
    """
    console.print('\n\n', scraper.title(), style="bold white", justify='center')

    console.print('\nINGREDIENTS', style="bold white")
    for index, ingredient in enumerate(scraper.ingredients()):
        console.print('-', ingredient, style='gold3')

    console.print('\nINSTRUCTIONS', style="bold white")
    for index, instruction in enumerate(scraper.instructions_list()):
        console.print(index+1, ') ', style='white', sep='', end='', highlight=False)
        console.print(instruction, style='gold3')


def main(url):

    #parser = argparse.ArgumentParser(description='Make recipes pretty again.')
    #parser.add_argument('operations', choices=['view', 'save'], nargs='+')

    #args = parser.parse_args()

    #if '--v' in args:
     #   view_in_terminal(url)

    #if '--s' in args:
     #   save_to_markdown

    save_to_markdown()
    

main(recipe_url)

