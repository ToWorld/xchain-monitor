# xchain-monitor

xchain-monitor是用来监控[xuperunion](https://github.com/xuperchain/xuperunion)区块链系统运行状态(包括机器、节点进程、节点业务信息)的开源监控系统。

-----------
## 监控指标，如下：

### 业务相关监控

* TrunkHeight
  - 节点当前最新区块高度；采用Graph表示；
* MaxBlockSize
  - 系统当前最大区块大小限制；采用Singlestat表示；
* AccountNewAmount
  - 创建一个合约账号需要消耗的资源；采用Singlestat表示；
* SetAclAmount
  - 设置权限ACL需要消耗的资源；Singlestat表示；
* TotalUtxoAmount
  - 当前系统utxo总量；采用Graph表示；
* UnconfirmedTxAmount
  - 当前节点未确认交易数量；采用Gauge表示；
* PostTxTPS
  - 当前节点交易TPS；采用Gauge表示；
* IrreversibleSlideWindow
  - 系统不可逆区块的窗口值；采用Singlestat表示；
* IrreversibleBlockHeight
  - 系统不可逆区块高度；采用Singlestat表示；
* UtxoLastBlockHash
  - 系统当前utxo最新区块ID；
* LedgerLastBlockHash
  - 系统当前ledger最新区块ID；
* AverageLatency
  - 系统平均延时；采用Graph表示；
