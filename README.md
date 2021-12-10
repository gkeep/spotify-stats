# spotify-stats

Spotify-stats is a small program made to display your top 10 tracks and artists from last 4 weeks (*short term*), last 6 months (*medium term*) and all time (*long term*).

![Top 10 tracks screenshot](image/top-tracks-screenshot.png)

## Libraries used
1. PyQt5
2. [Spotipy](https://spotipy.readthedocs.io/) - Python library for the Spotify Web API

# For developers
To work on spotify-stats you need to set up [pyenv](https://github.com/pyenv/pyenv) and virtualenv.

1. Install Python >= 3.6 using *pyenv*: `pyenv install 3.7.0`
2. Select installed version of Python: `pyenv local 3.7.0`
3. Install virtualenv and create new venv for the repository: `$(pyenv which python) -m pip install virtualenv`, `$(pyenv which python) -m virtualenv venv`
4. Activate virtualenv and install dependencies: `. venv/bin/activate`, `pip install -r requirements.txt`
5. Build using `make`: `make build`


# LICENSE
MIT license. See [LICENSE](LICENSE) for more information.
