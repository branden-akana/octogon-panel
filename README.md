
Octogon Panel
=============

super early stuff

![Preview Screenshot](preview.png)

## Requirements

- Python 3
- Requests (`pip install requests`)
- Jinja2 (`pip install jinja2`)

## Usage

save a smash.gg API key to a file named `dev-key.txt` to be able to query the smash.gg API.

serves to port 8000.

start server with `python client.py`

intended for use with the "browser source" source in OBS:
- connect to `localhost:8000` for a matchmaking overlay.
- connect to `localhost:8000/countdown` for a countdown overlay.
- connect to `localhost:8000/bracket` for a bracket overlay.

## Customization

stylesheet located in `style.css`. (beware: it is messy)

