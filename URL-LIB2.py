########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->           URL-LIB              <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import urllib2

url = 'LINK' #LINK EX: http(s)://www.google.com.br/

HEADER = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
             }

REQUEST = urllib2.Request(url, headers=HEADER)

ANSWER = urllib2.urlopen(REQUEST)

html = ANSWER.read()

print html