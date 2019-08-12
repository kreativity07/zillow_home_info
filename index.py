## Run this script in terminal with -------> python -c 'import index; index.api_invoke()'


import zillow
import configparser
import pprint

def api_invoke():

    config = configparser.ConfigParser()
    config.read('./api_key.conf')
    key = config.get('Zillow_API_Key_ZWSID','api_key')
    
    api = zillow.ValuationApi()

    address = "16229 North 22nd drive, Phoenix, AZ"
    postal_code="85023"

    data = api.GetSearchResults(key, address, postal_code)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint((data.get_dict()))

    detail_data = api.GetZEstimate(key, data.zpid)
    pp.pprint(detail_data.get_dict())

    comp_data = api.GetComps(key, data.zpid)
    pp.pprint(detail_data.get_dict())
        
    deep_results = api.GetDeepSearchResults(key, address, postal_code)
    pp.pprint(deep_results.get_dict())

