[Course TOC, Code, and Resources](https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/README.md)

# Brownie

- currently the most popular smart contract development platform built based on python. It heavily relies on **web3.py**

It's incredibly powerful and make our life much easier (comparing to what we did in web3_py_simply storage).

## pipx

- a tool to help you install and run end-user applications written in Python. It is recommended to install Brownie via pipx. Pipx is a tool to help you install and run end-user applications written in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s apt.

- pipx installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.

- difference from pip: pip is a general-purpose package installer for both libraries and apps with no environment isolation. pipx is made specifically for application installation, as it adds isolation yet still makes the apps available in your shell: pipx creates an isolated environment for each application and its associated packages.

# Prerequisites/Dependencies

## For Brownie

- `>>>python3 -m pip install --user pipx`
- `>>>python3 -m pipx ensurepath`
- restart terminal then
- `>>>pipx install eth-brownie` (or if that doesn't work, via pip `pip install eth-brownie`)

  - error message:
    The virtual environment was not created successfully because ensurepip is not available. On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.

    apt install python3.8-venv

    You may need to use sudo with that command. After installing the python3-venv package, recreate your virtual environment.

- `>>>apt install python3.8-venv`, then again
- `>>>pipx install eth-brownie`, then close and reopen the terminal
- `>>>brownie` to see all the available commands of brownie

## For previous web3_py_simple_storage

- Python/Python3
- `>>> sudo apt install npm (install Node.js and npm)`
- pip
- Ganache (local test network)
- GUI: download the AppImage and run it
- CLI: `>>> npm install -g ganache-cli` (need root access, >>>sudo su first), or
  - `>>>npm install --global yarn`(need root permission)
  - `>>>yarn global add ganache-cli`
- `>>>pip install py-solc-x (python solidity compiler)`
- `>>>pip install web3`
- `>>>pip install python-dotenv` (for managing private_key in the env)
- MetaMask
- infura

# SimpleStorage

## Setup, compile, and deploy

- `>>>brownie init` initialize brownie project (the folder **needs to be empty!!**). Folders created from the initialization:

  - build (important low level info)
    - contracts (store all compiled codes)
    - deployments (track all our deployments across all diff chains, store all compiled codes)
    - interfaces
  - contracts (store all the contracts, where Brownie will look for contract to compile and deploy)
  - interfaces (store all the interfaces)
  - reports
  - scripts (automate tasks such as deployments, calling functions, etc.)
  - test

- `>>>brownie compile` to compile the contract (SimpleStorage.sol) in contracts folder. Compiled contract info (e.g. "abi", "opcodes") stored in build/contracts/SimpleStorage.json
- `>>>brownie run scripts/deploy.py` to run the deploy script

## Testing

- Remix can do the test too. But writing test in smart contract development framework languages (Python, JavaScript) is better - allows more customization, control, typical CI/CD pipelines etc.
- tests/test_simple_storage.py, **test** at the beginning of testing scripts is **mandatory**
- `>>>brownie test` to run the testing script (no print() output from this commands)
- other useful commands:
  - `>>>brownie test -k test_updating_storage` (only test "test_updating_storage" function)
  - `>>>brownie test --pdb` (if the result is not pass, it will put us in a pythons shell for debugging)
  - `>>>brownie test –s` (detailed output, including print() results)
- [pytest](https://docs.pytest.org/en/6.2.x/contents.html) (which Brownie test is based on)documentation has more info

## Networks

- Brownie is prepackaged a list of networks that it is compatible with.
- `brownie networks list` to see them. **Development networks**, which brownie deploys contracts to by default, are temporary; while **Ethereum networks** (including the testnet) are persistent. Brownie going to track them.
- `brownie run scripts/deploy.py --network rinkeby` to deploy the contract to Rinkeby network
- deployment info is stored in folder deployments/4 (4 is the chain id of Rinkeby)

## Interacting with deployed contract

- `>>>brownie run scripts/read_value.py --network rinkeby`

- **brownie console**
  - for ad hoc tasks, we can use the brownie console to interact with the contracts
  - `$brownie console` (for Ganache local network)
  - basically we can run all lines in the python script (brownie modules, as we imported them in our scripts such as accounts, are aleady imported into this console)
    - `>>>account = accounts[0]`
    - `>>>account`
    - `>>>simple_storage = SimpleStorage.deploy({'from':account}) `
    - `>>>simple_storage`
    - `>>>SimpleStorage`
    - `>>>len(SimpleStorage)`
    - `>>>simple_storage.retrieve()` # 0
    - `>>>transaction = simple_storage.store(20, {"from": account})`
    - `>>>simple_storage.retrieve()` # 20
  - brownie shell is also a python shell, so we can run python code there, e.g. print('hello')

# FundMe

## Dependency / remapping

- Brownie doesn't recognize the npm download "import @chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol; But can for github download, so specify in brownie-config.yaml:

  `dependencies:# - <organization/repo>@<version> smartcontractkit/chainlink-brownie-contracts@1.1.1`
  `compiler: solc: remappings: - '@chainlink=smartcontractkit/chainlink-brownie-contracts@1.1.1'`

- after `$brownie compile`, will see both solidity files ("AggregatorV3Interface.sol" and "SafeMathChainlink.sol") in folder build/contracts/dependencies/smartcontractkit/chainlink-brownie-contracts@1.1.1

## Importing functions from scripts

- Separate `get_account()` into a separate file **helpful_scripts.py**
- Add an \***\*init**.py**, so FundMe.py can import functions **helpful_scripts.py\*\*

## Contract verification (publish_source) - code **"flattening"**

1. Manual way
   - rinkeby.etherscan -> Contract tab -> Verify and Publish -> copy/paste code. But it doesn't recognize "@chainlink...", so need to copy/paste the code of "AggregatorV3Interface.sol" and "SafeMathChainlink.sol at the top.
2. Programtic Way
   - add a line in our .env file `export ETHERSCAN_TOKEN=my etherscan.io API Key`
   - modify deploy_fund_me(), `fund_me=FundMe.deploy({'from':account}, publish_source=True)`
   - deploy the contract one more time, now at our contract page (address 0x7727A40640109FF6e3927f0572120ffa2BA80F7d) on rinkeby etherscan, there is a green check mark on the Contract tab. Click, and you'll see ALL the code there.

## Mocking

- deploy a fake contract (priceFeed) at local Ganache chain and interact with it as if it's real
- Constructor Parameters
- mock contract at: contracts/test/MockV3Aggregator.sol, this has all the same functions as real price feed contract
- for more info, see [ChainlinkMix](https://github.com/smartcontractkit/chainlink-mix)
- `brownie run scripts/deploy_FM.py` deploy contract to local Ganache Mock

## Add Ganache network to Brownie Ethereum

- `$brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337`
- check the result `brownie networks list`, will see ganache-local under Ethereum section
- update `if network.show_active() != "development":` to `if network.show_active() != LOCAL_BLOCKCHAIN_ENVIRONMENTS` (which is ["development", "ganache-local"])
- update `if network.show_active() == "development"` to `if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS`
- add `ganache-local: verify:False` to config file
- `$brownie run scripts/deploy_FM.py --network ganache-local` now brownie can keep track of deployments to Ganace in build/contracts/developments/1337 folder
