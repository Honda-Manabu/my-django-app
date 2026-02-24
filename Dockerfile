# 1. ベースとなる画像（Python 3.12）
FROM python:3.12-slim

# 2. 環境変数の設定（Pythonがログを即座に出力するようにする）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. コンテナ内の作業ディレクトリを作成・設定
WORKDIR /app

# 4. 依存関係のインストールに必要なシステムパッケージを導入（PostgreSQL用）
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. requirements.txtをコピーしてライブラリをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# PostgreSQL接続用のライブラリを追加でインストール
RUN pip install psycopg2-binary

# 6. プロジェクトの全ファイルをコンテナにコピー
COPY . /app/

# 7. Djangoを起動するコマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]