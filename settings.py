from os.path import join
import logging

########################################################################################################################
# Connection/Auth
########################################################################################################################

# API URL.
BASE_URL = "https://www.bitmex.com/api/v1/"


# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/app/apiKeys to fill these out.
API_KEY = ""
API_SECRET = ""

# What is the maximum duration of price/interest you can see on the chart
# Default saves 1 hour of time on the chart
SAVE_CHART_IN_SECONDS = 3600

# Charting color of price and interest
# Available colors :
# "blue"
# "orange"
# "green"
# "red"
# "purple"
# "brown"
# "pink"
# "gray"
# "olive"
# "cyan"
PRICE_LINE_COLOR = "green"
INTEREST_LINE_COLOR = "red"


LOG_LEVEL = logging.INFO
CONTRACTS = ["XBTUSD"]