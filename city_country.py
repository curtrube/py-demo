from operator import ne
from webbrowser import get


def get_formatted_city_country(city, country, population=""):
    """Neatly formats a city, country"""
    if population:
        formatted_city_country = f"{city}, {country} - population {population}"

    else:
        formatted_city_country = f"{city}, {country}"

    return formatted_city_country.title()
