clean-build:
	pyinstaller src/main.py \
		--paths "/home/gkeep/.cache/pypoetry/virtualenvs/spotify-stats-kcGKxyUI-py3.10/lib/python3.10/site-packages" \
		--name "spotify-stats" \
		--noconfirm \
		--onefile \
		--clean
