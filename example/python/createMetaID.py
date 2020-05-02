import bitsv
import time
from ecies import encrypt, decrypt

root = ("wif_key", "address")
info = ("wif_key", "address")
name = ("wif_key", "address")
protocol = ("wif_key", "address")
sample_protocol = ("wif_key", "address")
sample_protocol_detail = ("wif_key", "address")


def checkOne(object):
    assert type(object) == tuple
    assert len(object) == 2
    my_key = bitsv.Key(object[0])
    if my_key.address == object[1]:
        return True
    else:
        return False


def check():
    if checkOne(root) and checkOne(info) and checkOne(name) and checkOne(protocol) and checkOne(
            sample_protocol) and checkOne(sample_protocol_detail) :
        print("All check pass")
        return True
    else:
        return False


def createNode(my_key, address, tx, node_name, encrypt, data, version='0.09', data_type='text/plain', encoding='UTF-8'):
    #  <MetaID Flag><node_name><data><encrypt><version><data_type><encoding>
    Meta = 'meta'
    MetaIDTag = 'MetaID'

    pushdata = ([Meta.encode('utf-8'),
                 address.encode('utf-8'),
                 tx.encode('utf-8'),
                 MetaIDTag.encode('utf-8'),
                 node_name.encode('utf-8'),
                 data.encode('utf-8'),
                 encrypt.encode('utf-8'),
                 version.encode('utf-8'),
                 data_type.encode('utf-8'),
                 encoding.encode('utf-8')])

    tx_hash = my_key.send_op_return(pushdata)
    return tx_hash


if __name__ == '__main__':

    root_key = bitsv.Key(root[0])
    root_tx = createNode(root_key, root_key.public_key.hex(), 'NULL', 'Root', '0', 'NULL', 'NULL')
    print("root: \t\t" + root_tx)
    # info
    info_key = bitsv.Key(info[0])
    info_tx = createNode(root_key, info_key.public_key.hex(), root_tx, 'Info', '0', 'NULL', 'NULL')
    print("info: \t\t" + info_tx)

    # name
    name_key = bitsv.Key(name[0])
    name_tx = createNode(info_key, name_key.public_key.hex(), info_tx, 'name', '0', 'Alice')
    print("name: \t\t" + name_tx)

    # protocol
    protocol_key = bitsv.Key(protocol[0])
    protocol_tx = createNode(root_key, protocol_key.public_key.hex(), root_tx, 'Protocols', '0', 'NULL', 'NULL')
    print("protocol: \t\t" + protocol_tx)

    # sample_protocol
    sample_protocol_key = bitsv.Key(sample_protocol[0])
    brfc_sample_protocol = '001d46ffebf4'
    # title: = "SampleProtocol"
    # author: = "ShowPayTeam"
    # version: = "0.09"
    sample_protocol_tx = createNode(protocol_key,
                                    sample_protocol_key.public_key.hex(),
                                    protocol_tx,
                                    'SampleProtocol',
                                    '0',
                                    brfc_sample_protocol)
    print("sample_protocol: \t\t" + sample_protocol_tx)

    # sample_detail
    detailString = '{"content":"this is test","createTime":1587610622123}'
    sample_detail_key = bitsv.Key(sample_protocol_detail[0])
    sample_protocol_tx = createNode(sample_protocol_key,
                                    sample_detail_key.public_key.hex(),
                                    sample_protocol_tx,
                                    sample_detail_key.public_key.hex(),
                                    '0',
                                    detailString)
    print("sample_detail: \t\t" + sample_protocol_tx)
