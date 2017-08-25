PREFIX=/usr/local

install:
	@install -Dm755 ansible-keyring.py $(PREFIX)/bin/ansible-keyring
	@echo "Installed as $(PREFIX)/bin/ansible-keyring"

uninstall:
	@rm $(PREFIX)/bin/ansible-keyring
	@echo "Uninstalled"
