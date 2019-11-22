# xchain-monitor

xchain-monitor是用来监控[xuperunion](https://github.com/xuperchain/xuperunion)区块链系统运行状态(包括机器、节点进程、节点业务信息)的开源监控系统。

-----------
## 监控指标，如下：

* TrunkHeight
  - 节点当前最新区块高度；
* MaxBlockSize
  - 系统当前最大区块大小限制；
* AccountNewAmount
  - 创建一个合约账号需要消耗的资源；
* SetAclAmount
  - 设置权限ACL需要消耗的资源；
* TotalUtxoAmount
  - 当前系统utxo总量；
* UnconfirmedTxAmount
  - 当前节点未确认交易数量；
* PostTxTPS
  - 当前节点交易TPS；
* IrreversibleSlideWindow
  - 系统不可逆区块的窗口值；
* IrreversibleBlockHeight
  - 系统不可逆区块高度；
* UtxoLastBlockHash
  - 系统当前utxo最新区块ID；
* LedgerLastBlockHash
  - 系统当前ledger最新区块ID；
* AverageLatency
  - 系统平均延时
