########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->       REQUEST EXEMPLE          <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import requests

url = 'LINK' #LINK EX: http(s)://www.google.com.br/

HEADER = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
             }
PARAMETERS = {'id': '10'}

ANSWER = requests.get(url, headers=HEADER)

print ANSWER.text