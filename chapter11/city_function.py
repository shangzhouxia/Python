def get_city_name(city, country, population=''):
    if population:
        city_name = f"{city}, {country}-population {population}"
    else:
        city_name = f"{city}, {country}"
    return city_name.title()
