# MetaID-Example V0.1

#### 0.MetaID 数据部分格式定义

```
 <MetaID Flag><node_name><data><encrypt><version><data_type><encoding>  
```

为MetaID作为Metanet协议所增加的内容，具体含义如下：


| key       | value                                                        |
| --------- | ------------------------------------------------------------ |
| MetaIDTag | 固定为"MetaID"                                               |
| nodeName  | 节点标识名字                                                 |
| data      | 节点所对应的数据内容                                         |
| encrypt   | 标识该节点内容是否加密。本协议版本支持两种方式：0为不加密，1为ECIES加密。如采用ECIES加密，加密源为对应节点的公钥，采用对应节点的私钥解密。 |
| version   | 节点类型的版本号，不同版本号意味着data内容的格式不相同。数字 |
| data_type | 数据类型                                                     |
| encoding  | 数据编码                                                     |

#### 1 创建rootNode

**root 节点规定使用hd钱包 0/0 路径**，其他Node的路径可以自定义。

data 内容  对应协议

```
MetaID Root NULL 0 NULL text/plain UTF-8
```

获取rootID

e.g.

https://whatsonchain.com/tx/57fab4aab7af94f7ed885cfc32ff6b15a4d90d400dea652f85390b4bec7b1051

在例子中 rootID 为 “57fab4aab7af94f7ed885cfc32ff6b15a4d90d400dea652f85390b4bec7b1051”

#### 2 创建 infoNode

**在metenet/metaID中 infoNode 是 rootNode的子节点**

node_name为Info

data内容

```
MetaID Info NULL 0 NULL text/plain UTF-8
```

e.g.

https://whatsonchain.com/tx/a5c05146de8fa49d8641cf34ae556c982048cd74a22731285dd744a48b5ed400

infoNode 为 “a5c05146de8fa49d8641cf34ae556c982048cd74a22731285dd744a48b5ed400”

#### 3 创建nameNode

**在metenet/metaID中 nameNode 是 infoNode的子节点**

node_name 为 name , \<data\> 数据为用户昵称

data内容

```
MetaID name Alice 0 0.09 text/plain UTF-8
```

e.g.

https://whatsonchain.com/tx/cbbc2ca81876791e691d06087eeda502cf8d86c4b475c35a016ab8ba13dc3ab0

nameNode为 “cbbc2ca81876791e691d06087eeda502cf8d86c4b475c35a016ab8ba13dc3ab0”

#### 4 创建protocolsNode

**protocolsNode 是 rootNode的子节点**

node_name 为 Protocols

e.g.

https://whatsonchain.com/tx/35cfa27d059be2e8af4490fc482253a9c047b30c59ceb64869a66885723a4e89

nameNode为 “35cfa27d059be2e8af4490fc482253a9c047b30c59ceb64869a66885723a4e89”

#### 5 创建sampleProtocolNode

**sampleProtocolNode 是 protocolsNode的子节点**

node_name 为 自定义数据， data为协议对应的brfcid

e.g.

https://whatsonchain.com/tx/e995bbeb74da058900e9fec42e1d3be46689b7b5ee0c3899c483a9229323af9b

nameNode为 “e995bbeb74da058900e9fec42e1d3be46689b7b5ee0c3899c483a9229323af9b”

#### 6 创建sampleProtocolTxNode

**sampleProtocolTxNode 是 sampleProtocolNode的子节点**

e.g.

https://whatsonchain.com/tx/87b06ecfa3783a41c34235c1846b9f6daee773be7d74d65e482f6805b43b7422

nameNode为 “87b06ecfa3783a41c34235c1846b9f6daee773be7d74d65e482f6805b43b7422”

