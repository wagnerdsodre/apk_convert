import json
import certifi
from kivy.app import App
import urllib

from Custom_Layouts import BgBoxLayout
from kivy.network.urlrequest import UrlRequest


class Interface(BgBoxLayout):
    def clear(self):
        self.ids.textInput.text = ''
        self.ids.label.text = ''

    def fetched(self, req_body, result):
        print(result[0])
        polarity = str(result[0])
        subjectivity = str(result[1])
        self.ids.label.text = f'Polarity:{polarity} \n Subjectivity:{subjectivity} '

    def analyzer(self):
        params = json.dumps({'sentence': str(self.ids.textInput.text)})
        print(params)
        url = 'https://analyzer-psi.vercel.app/analyze/'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        UrlRequest(url, on_success=self.fetched, req_body=params,
                   req_headers=headers, ca_file=certifi.where(), verify=True)


class layout(App):
    pass


if __name__ == '__main__':
    layout().run()
