[Course TOC, Code, and Resources](https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/README.md)

**Brownie**

- currently the most popular smart contract development platform built based on python. It heavily relies on **web3.py**

It's incredibly powerful and make our life much easier (comparing to what we did in web3_py_simply storage).

**pipx**

- a tool to help you install and run end-user applications written in Python. It is recommended to install Brownie via pipx. Pipx is a tool to help you install and run end-user applications written in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s apt.

- pipx installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.

- difference from pip: pip is a general-purpose package installer for both libraries and apps with no environment isolation. pipx is made specifically for application installation, as it adds isolation yet still makes the apps available in your shell: pipx creates an isolated environment for each application and its associated packages.

**Prerequisites/Dependencies**

1. For Brownie

- `$python3 -m pip install --user pipx`
- `$python3 -m pipx ensurepath`
- restart terminal then
- `$pipx install eth-brownie` (or if that doesn't work, via pip `pip install eth-brownie`)

  - error message:
    The virtual environment was not created successfully because ensurepip is not available. On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.

    apt install python3.8-venv

    You may need to use sudo with that command. After installing the python3-venv package, recreate your virtual environment.

- `$apt install python3.8-venv`, then again
- `$pipx install eth-brownie`, then close and reopen the terminal
- `$brownie` to see all the available commands of brownie

2. For previous web3_py_simple_storage

   - Python/Python3
   - `$ sudo apt install npm (install Node.js and npm)`
   - pip
   - Ganache (local test network)
   - GUI: download the AppImage and run it
   - CLI: `$ npm install -g ganache-cli` (need root access, $sudo su first), or
     - `$npm install --global yarn`(need root permission)
     - `$yarn global add ganache-cli`
   - `$pip install py-solc-x (python solidity compiler)`
   - `$pip install web3`
   - `$pip install python-dotenv` (for managing private_key in the env)
   - MetaMask
   - infura

**SimpleStorage**

- `$brownie init` initialize brownie project (the folder **needs to be empty!!**)

  folders created from the initialization:

  - build (important low level info)
    - contracts (store all compiled codes)
    - deployments (track all our deployments across all diff chains, store all compiled codes)
    - interfaces
  - contracts (store all the contracts, where Brownie will look for contract to compile and deploy)
  - interfaces (store all the interfaces)
  - reports
  - scripts (automate tasks such as deployments, calling functions, etc.)
  - test

- `$brownie compile` to compile the contract (SimpleStorage.sol) in contracts folder. Compiled contract info (e.g. "abi", "opcodes") stored in build/contracts/SimpleStorage.json
- `$brownie run scripts/deploy.py` to run the script
