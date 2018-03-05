import json
import urllib
import httplib2
from pprint import pprint

def get_ecobici_availability():
    http = httplib2.Http()

    TOKEN_URL = "https://pubsbapi.smartbike.com/oauth/v2/token"

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    parameters = urllib.urlencode({'client_id': 'INSERT_HERE_YOUR_CLIENT_ID',
        'client_secret': 'INSERT_HERE_YOUR_CLIENT_SECRET',
        'grant_type': 'client_credentials'})

    resp, response_token = http.request(TOKEN_URL, method='POST', body=parameters, headers=headers)

    token_data = json.loads(response_token)

    ACCESS_TOKEN = token_data['access_token']

    #print ACCESS_TOKEN

    headers_access = {'Authorization': 'Bearer ' +ACCESS_TOKEN}

    STATIONS_LIST = "https://pubsbapi.smartbike.com/api/v1/stations.json"
    STATUS_STATIONS = "https://pubsbapi.smartbike.com/api/v1/stations/status.json"

    resp, response_token = http.request(STATUS_STATIONS, method='GET', headers=headers_access)


    status_data = json.loads(response_token)
    # 433 Electricas Jose Ma Olloqui
    # 432 Normales Jose Ma Olloqui
    # 32 Electricas Florencia - Londres
    # 448 Electricas Acapulco Puebla
    # 22 Oficina
    # 27 IMSS Toledo
    # 37 Cozumel-Puebla

    # https://www.tablesgenerator.com/html_tables#

    response = "<html>"
    response += "<head>"
    response += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    response += "<style type='text/css'>"
    response += ".tg {"
    response += "    border-collapse: collapse;"
    response += "    border-spacing: 0;"
    response += "    border-color: #999;"
    response += "}"
    response += ".tg td {"
    response += "    font-family: Arial, sans-serif;"
    response += "    font-size: 14px;"
    response += "    padding: 10px 5px;"
    response += "    border-style: solid;"
    response += "    border-width: 1px;"
    response += "    overflow: hidden;"
    response += "    word-break: normal;"
    response += "    border-color: #999;"
    response += "    color: #444;"
    response += "    background-color: #F7FDFA;"
    response += "}"
    response += ".tg th { "
    response += "    font-family: Arial, sans-serif;"
    response += "    font-size: 14px;"
    response += "    font-weight: normal;"
    response += "    padding: 10px 5px;"
    response += "    border-style: solid;"
    response += "    border-width: 1px;"
    response += "    overflow: hidden;"
    response += "    word-break: normal;"
    response += "    border-color: #999;"
    response += "    color: #fff;"
    response += "    background-color: #26ADE4;"
    response += "}"
    response += ".tg .tg-404i {"
    response += "    font-weight: bold;"
    response += "    font-family: 'Trebuchet MS', Helvetica, sans-serif !important;"
    response += "    ;"
    response += "    vertical-align: top"
    response += "}"
    response += ".tg .tg-o9ov {"
    response += "    font-family: 'Trebuchet MS', Helvetica, sans-serif !important;"
    response += "    ;"
    response += "    vertical-align: top"
    response += "}"
    response += "@media screen and (max-width: 767px) {.tg {width: auto !important;}"
    response += ".tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;}}"

    response += "</style>"

    response += "</head>"
    response += "<body>"

    response += "<table class='tg'>"
    response += "<tr>"
    response += "    <th class='tg-404i' colspan='2'>Bicicletas Disponibles</th>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Toledo</td>"
    response += "   <td class='tg-404i'>"+str(status_data["stationsStatus"][27]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Oficina</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][22]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Elec. Florencia-Londres</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][32]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Elec. Acapulco-Puebla</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][448]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Cozumel-Puebla</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][37]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Elec. Jos&eacute; Ma. Olloqu&iacute;</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][433]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "<tr>"
    response += "    <td class='tg-o9ov'>Jos&eacute; Ma. Olloqu&iacute;</td>"
    response += "    <td class='tg-404i'>"+str(status_data["stationsStatus"][432]['availability']['bikes'])+"</td>"
    response += "</tr>"
    response += "</table>"


    response += "</body></html>"

    return response


def endpoint(event, context):
    data = get_ecobici_availability()

    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/html',
        },
        "body": data
    }
    return response
