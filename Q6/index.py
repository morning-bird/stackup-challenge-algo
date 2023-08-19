from algosdk import account, mnemonic

def generate_algorand_keypair():
  # Generate the account
  private_key, address = account.generate_account()

  # Print out the account address, private key, and mnemonic
  print("My address: {}".format(address))
  print("My private key: {}".format(private_key))
  print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

generate_algorand_keypair()
