# ansible-keyring
Can be used as wrapper between ansible and gnome keyring.

But also with the following backends (supported by python-keyring)
   * Mac OS X Keychain
   * Freedesktop Secret Service (requires secretstorage)
   * KWallet (requires dbus)
   * Windows Credential Vault

Usage
-----

### Store password in (gnome-)keyring
    ansible-keyring set password-name
    
### Usage with Ansible for vault
Create the following script (eg. ~/.ansible_vault) and make it executable

    #!/bin/bash
    ansible-keyring get password-name
    # Set environment variable
    export ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault   
