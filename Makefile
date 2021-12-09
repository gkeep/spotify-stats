.PHONY: clean build install-cfg run

build:
	make clean
	python setup.py build

run:
	build/exe.linux-x86_64-$$(pyenv local | cut -c -3)/spotify-stats

clean:
	rm -f build/exe.linux-x86_64-$$(pyenv local | cut -c -3)/spotify-stats

install-cfg:
	mkdir -p "$$XDG_CONFIG_HOME/spotify-stats"
	cp .env "$$XDG_CONFIG_HOME/spotify-stats/env"