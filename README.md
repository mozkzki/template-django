# django-template

## Development

### Prerequisites

- pipenv

### Preparation

プロジェクトディレクトリごとに仮想環境を作成するための環境変数追加

#### Linux

```(sh)
export PIPENV_VENV_IN_PROJECT=true
```

#### Windows

```(sh)
set PIPENV_VENV_IN_PROJECT=true
```

1. `git clone git@github.com:yukkun007/django-template.git`
1. `pip install pipenv`
1. `pipenv install --dev`

### test execution

```(sh)
pipenv run start
```

下記にアクセス

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/event/
- http://127.0.0.1:8000/event/table/

### unit test

```(sh)
pipenv run ut
```

### lint

```(sh)
pipenv run lint
```

## 参考

### Django プロジェクト作成

```(sh)
django-admin startproject <project_name>
```

### Django アプリケーション作成

```(sh)
python manage.py startapp <app_name>
```
