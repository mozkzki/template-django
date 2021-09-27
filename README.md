# template-django

Djangoのテンプレート (サンプル)

- [Django ドキュメント](https://docs.djangoproject.com/ja/3.2/)

## Install

```sh
pip install git+https://github.com/mozkzki/template-django
# upgrade
pip install --upgrade git+https://github.com/mozkzki/template-django
# uninstall
pip uninstall template-django
```

## Usage

```sh
python ./manage.py runserver
# or
make start
```

下記にアクセス

- <http://127.0.0.1:8000/>
- <http://127.0.0.1:8000/get/>
- <http://127.0.0.1:8000/get/?user=hoge>
- <http://127.0.0.1:8000/event/>
- <http://127.0.0.1:8000/event/table/>

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./manage.py runserver
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src
# or
make lint
```

### Update dependency modules

dependabot (GitHub公式) がプルリクを挙げてくるので確認してマージする。

- dependabotは`pyproject.toml`と`poetry.lock`を更新してくれる

## 参考

Django プロジェクト作成

```sh
django-admin startproject <project_name>
```

Django アプリケーション作成

```sh
python manage.py startapp <app_name>
```
