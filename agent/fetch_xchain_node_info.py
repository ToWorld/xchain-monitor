import requests
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Gauge
from flask import Response, Flask
import json
import os

REGISTRY = CollectorRegistry(auto_describe=False)
Balance = Gauge("balance", "the address's address", registry=REGISTRY)
TrunkHeight = Gauge("trunkHeight", "latest block height", registry=REGISTRY)
MaxBlockSize = Gauge("maxBlockSize", "maxmium block size", registry=REGISTRY)
AccountNewAmount = Gauge("accountNewAmount", "amount of new a contract account", registry=REGISTRY)
SetAclAmount = Gauge("setAclAmount", "amount of set an acl", registry=REGISTRY)
TotalUtxoAmount = Gauge("totalUtxoAmount", "amount of total utxo", registry=REGISTRY)
UnconfirmedTxAmount = Gauge("unconfirmedTxAmount", "amount of unconfirmed tx", registry=REGISTRY)
PostTxTPS = Gauge("postTx", "tps of postTx", registry=REGISTRY)
IrreversibleSlideWindow = Gauge("irreversibleSlideWindow", "irreversible slide window", registry=REGISTRY)
IrreversibleBlockHeight = Gauge("irreversibleBlockHeight", "irreversible block height", registry=REGISTRY)
UtxoLastBlockHash = Gauge("uxtoLastBlockHash", "last blockid in utxo", registry=REGISTRY)
LedgerLastBlockHash = Gauge("ledgerLastBlockHash", "last blockid in ledger", registry=REGISTRY)
AverageLatency = Gauge("avgDelay", "average latency", registry=REGISTRY)

app = Flask(__name__)

def getBalance(url, chainName, address):
    payload = {
        'bcs':[{'bcname':chainName}],
        'address': address
    }
    balanceResponse = requests.post(url+"/v1/get_balance", data=json.dumps(payload))
    balance = json.loads(balanceResponse.content)
    return balance['bcs'][0]['balance']

def getMetaInfo(url, chainName):
    payload = {}
    metaInfoResponseBuf = requests.post(url+"/v1/get_sysstatus", data=json.dumps(payload))
    metaInfoResponse = json.loads(metaInfoResponseBuf.content)
    
    ledgerMeta = metaInfoResponse['systems_status']['bcs_status'][0]['meta']
    # step1: get trunkHeight
    try:
        trunkHeight = ledgerMeta['trunk_height']
    except Exception:
        trunkHeight = 0
    # step2: get ledgerLastBlockHash
    try:
        ledgerLastBlockHash = ledgerMeta['tip_blockid']
    except Exception:
        ledgerLastBlockHash = 0

    utxoMeta = metaInfoResponse['systems_status']['bcs_status'][0]['utxoMeta']
    # step3: get maxBlockSize
    try:
        maxBlockSize = utxoMeta['max_block_size']
    except Exception:
        maxBlockSize = 0
    # step4: get accountNewAmount
    try:
        accountNewAmount = utxoMeta['new_account_resource_amount']
    except Exception:
        accountNewAmount = 0
    # step5: get setAclAmount
    try:
        setAclAmount = accountNewAmount
    except Exception:
        setAclAmount = 0
    # step6: get totalUtxoAmount
    try:
        totalUtxoAmount = utxoMeta['utxo_total']
    except Exception:
        totalUtxoAmount = 0
    # step7: get unconfirmedTxAmount
    try:
        unconfirmedTxAmount = utxoMeta['unconfirmTxAmount']
    except Exception:
        unconfirmedTxAmount = 0
    # step8: get irreversibleSlideWindow
    try:
        irreversibleSlideWindow = utxoMeta['irreversibleSlideWindow']
    except Exception:
        irreversibleSlideWindow = 0
    # step9: get irreversibleBlockHeight
    try:
        irreversibleBlockHeight = utxoMeta['irreversibleBlockHeight']
    except Exception:
        irreversibleBlockHeight = 0
    # step10: get averageLatency
    try:
        averageLatency = utxoMeta['avgDelay']
    except Exception:
        averageLatency = 0
    # step11: get utxoLastBlockHash
    try:
        utxoLastBlockHash = utxoMeta['latest_blockid']
    except Exception:
        utxoLastBlockHash = 0

    return trunkHeight,ledgerLastBlockHash,maxBlockSize,accountNewAmount,setAclAmount,totalUtxoAmount,unconfirmedTxAmount,irreversibleSlideWindow,irreversibleBlockHeight,averageLatency,utxoLastBlockHash

@app.route("/xchain-monitor")
def exporter():
    balance = getBalance('http://localhost:8097', 'xuper', 'dpzuVdosQrF2kmzumhVeFQZa1aYcdgFpNbogon')
    Balance.set(balance)
    trunkHeight,ledgerLastBlockHash,maxBlockSize,accountNewAmount,setAclAmount,totalUtxoAmount,unconfirmedTxAmount,irreversibleSlideWindow,irreversibleBlockHeight,averageLatency,utxoLastBlockHash = getMetaInfo('http://localhost:8097', 'xuper')
    TrunkHeight.set(trunkHeight)
    #LedgerLastBlockHash.set(ledgerLastBlockHash)
    MaxBlockSize.set(maxBlockSize)
    AccountNewAmount.set(accountNewAmount)
    SetAclAmount.set(setAclAmount)
    TotalUtxoAmount.set(totalUtxoAmount)
    UnconfirmedTxAmount.set(unconfirmedTxAmount)
    IrreversibleSlideWindow.set(irreversibleSlideWindow)
    IrreversibleBlockHeight.set(irreversibleBlockHeight)
    AverageLatency.set(averageLatency)
    #UtxoLastBlockHash.set(utxoLastBlockHash)
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3531)
