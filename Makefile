help h:
	@echo "Available Commands:"
	@sed -n "/^[a-zA-Z0-9_.]*:/s/:.*//p" < Makefile | GREP_COLOR="01;34" grep --color=always -E "^[a-zA-Z0-9_.]*"

install:
	@echo "\e[1;34mInstalling Dependencies...\e[0m"
	@pip install -r requirements.txt

run:
	@python3 main.py