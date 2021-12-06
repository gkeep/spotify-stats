# spotify-stats

Spotify-stats is a small program made to display your top 10 tracks and artists from last 4 weeks (*short term*), last 6 months (*medium term*) and all time (*long term*).

![Top 10 tracks screenshot](image/top-tracks-screenshot.png)

## Libraries used
1. PyQt5
2. [Spotipy](https://spotipy.readthedocs.io/) - Python library for the Spotify Web API

# For developers
To work on spotify-stats you need to set up [pyenv](https://github.com/pyenv/pyenv) and [Poetry](https://python-poetry.org/).

1. Install Python >= 3.6 using *pyenv*: `pyenv install 3.7.0`
2. Select installed version of Python: `pyenv local 3.7.0`
3. Open Poetry shell and select installed Python version for the project: `poetry shell && poetry env use $(pyenv which python)`
4. Install dependencies: `poetry install`


# LICENSE
MIT license. See [LICENSE](LICENSE) for more information.
