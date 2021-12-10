.PHONY: clean build install-cfg run

build:
	make clean
	make install-cfg
	python setup.py build

run:
	build/exe.linux-x86_64-$$(pyenv local | cut -c -3)/spotify-stats

clean:
	rm -f build/exe.linux-x86_64-$$(pyenv local | cut -c -3)/spotify-stats

install-cfg:
	bash util/create_cfg.sh
