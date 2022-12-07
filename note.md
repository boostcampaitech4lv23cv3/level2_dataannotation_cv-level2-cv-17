```yaml
- repo: https://github.com/PyCQA/flake8
  rev: 5.0.4
  hooks:
    - id: flake8
      args:
        - "--max-line-length=88"
        - "--max-complexity=18"
```

https://rednafi.github.io/digressions/python/2020/04/06/python-precommit.html

```yaml
# black
- repo: https://github.com/ambv/black
  rev: stable
  hooks:
    - id: black
      args: # arguments to configure black
        - --line-length=88
        - --include='\.pyi?$'

        # these folders wont be formatted by black
        - --exclude="""\.git |
          \.__pycache__|
          \.hg|
          \.mypy_cache|
          \.tox|
          \.venv|
          _build|
          buck-out|
          build|
          dist"""

      language_version: python3.6

# flake8
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v2.3.0
  hooks:
    - id: flake8
      args: # arguments to configure flake8
        # making isort line length compatible with black
        - "--max-line-length=88"
        - "--max-complexity=18"
        - "--select=B,C,E,F,W,T4,B9"

        # these are errors that will be ignored by flake8
        # check out their meaning here
        # https://flake8.pycqa.org/en/latest/user/error-codes.html
        - "--ignore=E203,E266,E501,W503,F403,F401,E402"
```

https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ethos-u-vela/+/refs/heads/master/.pre-commit-config.yaml
https://blog.eunsukim.me/posts/lint-and-format-python-code-before-commit
https://stackoverflow.com/questions/71773712/simplifying-line-length-with-pre-commit-flake8-black-isort-pylint-etc

pyproject.toml

```toml
[tool.black]
line-length = 130
target-version = ['py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
| \.hg
| \.mypy_cache
| \.tox
| \.venv
| _build
| buck-out
| build
)/
'''

[tool.flake8]
max-line-length = 130
extend-ignore = ["D203", "E203", "E251", "E266", "E302", "E305", "E401", "E402", "E501", "F401", "F403", "W503"]
exclude = [".git", "__pycache__", "dist"]
max-complexity = 10

[tool.isort]
atomic = true
profile = "black"
line_length = 130
skip_gitignore = true
```
