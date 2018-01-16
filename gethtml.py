import requests

class getHtml:

    def get_html(self, url):
        r = requests.get(url)
        return r.text