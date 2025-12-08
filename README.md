# Hacker News Links Parser

parser for working with [hacker news](https://news.ycombinator.com/)

## Install:

### Linux:
```bash
python -m venv venv
pip install -r requirements.txt
```

### Windows:
```powershell
.\venv\Scripts\Activate.bat
pip install -r requirements.txt
```

### Linux:
```bash
source /D/MyRepo/RedditParser/venv/Scripts/activate
```
## Using:
- `-c` count first page 

```bash
python parser.py -c 2
page:1, find artice:30
page:2, find artice:60
```