#Carlos Cipriano
#ID: 0719076
#12/16/2019

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
