from algosdk.future import transaction
from algosdk import constants, mnemonic
from algosdk.v2client import algod
import json
import base64

# Connect to the Algod Client on the Algorand sandbox
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Declare your address and passphrase
my_address = "PI6LYV5CMWDIJMMS2RS4GI27Z6V2AGREEFQFJL56SMHK3UTUX4SNT6VL44"
my_passphrase = "slight pelican mimic yellow source reunion appear vicious slush senior rent hurry meat shadow ring fee enroll first hair loud rich kidney believe above present"

# Derive your private key from your passphrase
private_key = mnemonic.to_private_key(my_passphrase)

def your_first_transaction(private_key, my_address):
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    # params.flat_fee = True
    # params.fee = constants.MIN_TXN_FEE
    receiver = "MLP2H7ZP6VOMRBZWBT3SJ3IQH25KSWSNXH2REQRGNFQSJQJRLVALD2TM2M"
    note = "First PythonSDK Transaction (Ren)".encode()
    amount = 1000000
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)
    signed_txn = unsigned_txn.sign(private_key)
    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    account_info = algod_client.account_info(my_address)

    print("Transaction information: {}".format(
    json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
    confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transferred: {} microAlgos".format(amount) )
    print("Fee: {} microAlgos".format(params.fee) )
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')))

your_first_transaction(private_key, my_address)