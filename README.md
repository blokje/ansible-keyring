# ansible-keyring
Can be used as wrapper between ansible and gnome keyring.

But also with the following backends (supported by python-keyring)
   * Mac OS X Keychain
   * Freedesktop Secret Service (requires secretstorage)
   * KWallet (requires dbus)
   * Windows Credential Vault

Usage
-----
### Installation
    sudo make install
    make PREFIX=~/.local install # Installs in ~/.local/bin/

### Store password in (gnome-)keyring
    ansible-keyring set password-name
    
### Usage with Ansible for vault
Set the following environment variables:

    ANSIBLE_KEYRING_NAME=keyname
    ANSIBLE_VAULT_PASSWORD_FILE=$(which ansible-keyring)

#### Wrapper script
You can also create a wrapper script and make it executable

    #!/bin/bash
    ansible-keyring get password-name
    # Set environment variable

Point ansible to the wrapper script

    export ANSIBLE_VAULT_PASSWORD_FILE=~/path/to/wrapper_script
