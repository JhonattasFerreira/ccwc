
INSTALL_DIR = /usr/local/bin

SCRIPT_NAME = ccwc.py

SCRIPT_PATH = $(shell pwd)/$(SCRIPT_NAME)

TEST_CMD = python tests.py

test:
	$(TEST_CMD)

install:
	sudo ln -s $(SCRIPT_PATH) $(INSTALL_DIR)/ccwc

uninstall:
	sudo rm $(INSTALL_DIR)/ccwc
 
