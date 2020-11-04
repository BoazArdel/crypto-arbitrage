import requests
import json
import pprint
import pandas as pd
from passwords import API_KEY
#pandas.read_json("input.json").to_excel("output.xlsx")

response = requests.get("https://api.coinmetrics.io/v2/asset_info", headers={'Authorization': API_KEY},params={
  "assetsInfo": [
    {
      "id": "btc",
      "name": "Bitcoin",
      "metrics": [
        "BlkCnt",
        "PriceUSD",
        "TxCnt"
      ],
      "metrics_rt": [
        "BlkCnt"
      ],
      "metrics_flows": [
        "FlowInExNtv",
        "SplyExNtv"
      ],
      "metrics_flows_rt": [
        "FlowTfrToExCnt"
      ],
      "exchanges": [
        "coinbase",
        "gemini"
      ],
      "markets": [
        "coinbase-btc-usd-spot",
        "gemini-btc-usd-spot"
      ],
      "minTime": "2009-01-03T00:00:00Z",
      "maxTime": "2019-02-13T00:00:00Z"
    },
    {
      "id": "eth",
      "name": "Ethereum",
      "metrics": [
        "BlkCnt",
        "PriceUsd",
        "TxCnt"
      ],
      "metrics_rt": [
        "BlkCnt"
      ],
      "metrics_flows": [
        "FlowInExNtv",
        "SplyExNtv"
      ],
      "metrics_flows_rt": [
        "FlowTfrToExCnt"
      ],
      "exchanges": [
        "coinbase",
        "gemini"
      ],
      "markets": [
        "coinbase-eth-usd-spot",
        "gemini-eth-usd-spot"
      ],
      "minTime": "2015-08-07T00:00:00Z",
      "maxTime": "2019-03-01T00:00:00Z"
    }
  ]
}
)

response3 = requests.get("https://api.coinmetrics.io/v2/markets", headers={'Authorization': API_KEY})
print (response3.content)
json_text = response3.content
df = pd.read_json(json_text)
df.to_excel('output.xls', index=False)

# Print the status code of the response.
#data = json.loads(response.content)
#pprint.pprint(data)