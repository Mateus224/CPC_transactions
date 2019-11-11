#!/usr/bin/env python3

from cpc_fusion import Web3
import time

def executeSomething():
    #code here
    time.sleep(65)



def test_local_sendRawTransaction():
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8501'))
    # web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    # change the keypath to your keystore file
    with open('path/to/your/keystore') as keyfile:
        encrypted_key = keyfile.read()
    # print(web3.cpc.getBalance(web3.cpc.accounts))
    print(web3.cpc.accounts)
    print('balance:', web3.cpc.getBalance(web3.cpc.accounts[0]))
    print("================================encrypted_key======================\n")
    print(encrypted_key)
    private_key_for_senders_account = web3.cpc.account.decrypt(encrypted_key, 'password')
    print("private_key_for_senders_account:")
    print(private_key_for_senders_account)
    print('coinbase:', web3.cpc.coinbase)
    from_addr = web3.toChecksumAddress('0xCF1717B7dC2e17a53B0A9762e86C16d785ab9c3e') 
    to_addr = web3.toChecksumAddress('0xb3801b8743dea10c30b0c21cae8b1923d9625f84')

    print('gasPrice:', web3.cpc.gasPrice)
    # set chainId to None if you want a transaction that can be replayed across networks
    tx_dict = dict(
        type=0,
        nonce=web3.cpc.getTransactionCount(from_addr),
        gasPrice=web3.cpc.gasPrice,
        gas=900000,
        to=to_addr,
        value=1,
        data=b'',
        chainId=42,
    )
    signed_txn = web3.cpc.account.signTransaction(tx_dict,
                                                  private_key_for_senders_account,
                                                  )
    print("signed_txn:")
    print(signed_txn)

    print("sendRawTransaction:")
    print(web3.toHex(signed_txn.rawTransaction))
    print(web3.cpc.sendRawTransaction(signed_txn.rawTransaction))

if __name__=='__main__':
    starttime=time.time()
    while 1:
        test_local_sendRawTransaction()
        executeSomething()
