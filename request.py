import requests


class RequestAPI(object):
    api_url = 'http://127.0.0.1:8000/api/disease/'

    # Here the method using for fetch data from server
    def fetch_data(self):
        data = requests.get(self.api_url)
        if data.status_code == 200:
            return data.content
        elif data.status_code == 404:
            print(f"Not ok {data.status_code}")
        else:
            print('An error has occurred.')

if __name__ == '__main__':
    request_instance = RequestAPI()
    print(request_instance.fetch_data())


