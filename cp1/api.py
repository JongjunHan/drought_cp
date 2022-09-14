import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'

queryParams = '?' + \
              'ServiceKey=' + 'emOxiXsw1mwITVY9YQbZdlINaf%2BeMhqqxETj%2FLYPmiQf7pTsc%2Fcs4H13bUvAbNayx9afT1b5o8W7st9uzgXfHw%3D%3D' + \
              '&pageNo='+ '1' + \
              '&numOfRows='+ '999' + \
              '&dataType='+ 'JSON' + \
              '&dataCd='+ 'ASOS' + \
              '&dateCd='+ 'DAY' + \
              '&startDt='+ '19810101' + \
              '&endDt='+ '20211231' + \
              '&stnIds='+ '108' # \

url + queryParams

result = requests.get(url + queryParams)
js = json.loads(result.content)
data = pd.DataFrame(js['response']['body']['items']['item'])

print(data)
