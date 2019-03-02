import urllib.request,json
from .models import Quotes


# Getting api key
# Getting the quote base url
base_url = None

def configure_request(app):
    global api_key,base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_object = None

        if get_quotes_response:
           id=get_quote_response.get('id')
           author=get_quote_reponse.get('author')
           content=get_quote_response.get('quote')
           quote_object=Quote(id,author,content)           

        return quote_object