from typing import List

from subject import Internet
from real_subject import AccessToInternet


class ProxyInternet(Internet):
    __banned_url: List[str] = []

    def __init__(self):
        self.__internet: Internet = AccessToInternet()
        ProxyInternet.__banned_url.append('twitter.com')
        ProxyInternet.__banned_url.append('facebook.com')
        ProxyInternet.__banned_url.append('google.com')

    def connect_to(self, url: str):
        if url in ProxyInternet.__banned_url:
            raise Exception('URL bloqueada - Acceso Denegado - Consulta con tu administrador')
        self.__internet.connect_to(url)
