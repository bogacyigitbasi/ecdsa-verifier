All steps and detailed tutorial can be found on my Medium. Here is the link: https://medium.com/@bogachanyigitbasi/verify-signature-on-ethereum-using-foundry-454341cf80a2

# ECDSA Practice

- To create&activate the venv
  `python3 -m venv path/to/venv`
  `source path/to/venv/bin/activate`
- Install required python libraries
  `python3 -m pip install ecdsa eth-keys`

- We can use this tool to generate a pair of public private ECDSA keys
  https://emn178.github.io/online-tools/ecdsa/key-generator/

# Signing

Sign a message to generate the values of r, s which is the signature.

# Verification

For verification, one needs to receive the signature (r,s), signed message and public key.
It is possible to do it without receiving the public key if you know how to recover it. Using the algorithm shared in the next step.

# Re-compute Public Key

How a public key can be recovered, in Ethereum context how `ecrecover` function works under the hood.

# Solidity

## Foundry

**Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust.**

Foundry consists of:

- **Forge**: Ethereum testing framework (like Truffle, Hardhat and DappTools).
- **Cast**: Swiss army knife for interacting with EVM smart contracts, sending transactions and getting chain data.
- **Anvil**: Local Ethereum node, akin to Ganache, Hardhat Network.
- **Chisel**: Fast, utilitarian, and verbose solidity REPL.

## Documentation

https://book.getfoundry.sh/

## Usage

### Build

```shell
$ forge build
```

### Test

```shell
$ forge test
```

### Format

```shell
$ forge fmt
```

### Gas Snapshots

```shell
$ forge snapshot
```

### Anvil

```shell
$ anvil
```

### Deploy

```shell
$ forge script script/Counter.s.sol:CounterScript --rpc-url <your_rpc_url> --private-key <your_private_key>
```

### Cast

```shell
$ cast <subcommand>
```

### Help

```shell
$ forge --help
$ anvil --help
$ cast --help
```
