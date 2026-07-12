# Implementation Notes

`uv init` creates all of the following immediately:

1. git folder
2. .gitignore
3. .python-version
4. main.py
5. pyproject.toml
6. README.md

I then did:

`uv add pytest`
`uv add playwright`

I had trouble getting playwright to work, so I started the virtual environment with
`source .venv/bin/activate`
and then ran
`playwright install` and that seemed to work
