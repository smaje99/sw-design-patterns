from subject import Internet


class AccessToInternet(Internet):
    def connect_to(self, url: str):
        print(f'Conectando a: {url}')
