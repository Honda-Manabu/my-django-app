# 1. ベースとなる画像（Python 3.12）
FROM python:3.12

# 2. 環境変数の設定（Pythonがログを即座に出力するようにする）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. コンテナ内の作業ディレクトリを作成・設定
WORKDIR /app

# 4. 依存関係のインストールに必要なシステムパッケージを導入（PostgreSQL用）
<<<<<<< HEAD
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    libc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

=======
RUN apt-get update && apt-get install -y libpq-dev 
    
>>>>>>> f8af3c0b8da8e14916ae2e6f7326e470d73e0413
# 5. requirements.txtをコピーしてライブラリをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# PostgreSQL接続用のライブラリを追加でインストール
RUN pip install psycopg2-binary

# 6. プロジェクトの全ファイルをコンテナにコピー
COPY . /app/

# 7. Djangoを起動するコマンド
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# gunicornを起動:テスト時はdocker-compose.ymlで置き換わる
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_django_project.wsgi:application"]
