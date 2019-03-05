import urllib.request,json
from .models import Quote
from app import app

base_url=None
base_url = app.config['QUOTE_API_BASE_URL']
def configure_request(app):
   global base_url

  

def get_quote():
  with urllib.request.urlopen(base_url) as url:
    get_quote_data=url.read()
    get_quote_response=json.loads(get_quote_data)

    quote_object=None

    if get_quote_response:
       id=get_quote_response.get('id')
       author=get_quote_response.get('author')
       content=get_quote_response.get('quote')
       quote_object=Quote(id,author,content)

       return quote_object
