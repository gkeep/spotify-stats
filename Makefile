.PHONY: clean build install-cfg run

build:
	make clean

	pyinstaller src/main.py \
		--paths "$$(poetry env info --path)/lib/python$$(pyenv local | cut -c -3)/site-packages" \
		--hidden-import PyQt5.sip \
		--name "spotify-stats" \
		--noconfirm \
		--onefile \
		--clean

run:
	dist/spotify-stats

clean:
	rm -f dist/*

install-cfg:
	mkdir -p "$$XDG_CONFIG_HOME/spotify-stats"
	cp .env "$$XDG_CONFIG_HOME/spotify-stats/env"