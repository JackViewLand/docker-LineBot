# docker-LineBot

- [docker-LineBot](#docker-LineBot)
  - [說明](#說明)
  - [使用方法](#使用方法)
  - [資料夾結構](#資料夾結構)
  - [參考資料](#參考資料)


## 說明
---
- 使用docker 與docker-compose 進行部署。
- 使用```Nginx``` proxy 到```uWSGI```，再用```python flask```運行line bot。
- LINE Developers 串接時需要使用https進行訪問，請自行申請ssl 憑證。
- nginx log 與 uWSGI log 有掛載出來。

## 使用方法
---
### 前置動作：
#### 安裝docker與docker-compose
* 更新apt套件
```bash
sudo apt-get update
```
```bash
sudo apt-get -y install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

* 添加docker官方GPG密鑰
```bash
sudo mkdir -p /etc/apt/keyrings
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

* 添加docker的apt儲存庫
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

* 安裝Docker與Docker compose
```bash
sudo apt-get update
```
```bash
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
```bash
sudo ln -s /usr/libexec/docker/cli-plugins/docker-compose /usr/bin/docker-compose
```
* 確認是否安裝成功
```bash
sudo docker version
```
```bash
docker-compose version
```
* 新增群組docker
```bash
sudo groupadd docker
```
* 將指定帳戶加入群組
```bash
sudo usermod -aG docker <username>
```
* 更新用戶組
```bash
newgrp docker
```
*登入到帳戶執行docker確認是否成功
```bash
docker run hello-world
```
* 查看docker 用戶組
```bash
cat /etc/group | grep docker
```

#### 運行專案
* clone 專案
```bash
git https://github.com/JackViewLand/docker-LineBot.git
```
* 在專案資料夾底下新增.env檔案存放ACCESS_TOKEN與CHANNEL_SECRET
```bash
cd  docker-LineBot
```
```bash
touch .env
```
```bash
CHANNEL_ACCESS_TOKEN=''
CHANNEL_SECRET=''
```
* 請將域名申請的憑證放入nginx/cert
* 修改 nginx/flask_app.conf中YOUR_SERVERNAME成自己的域名
``` bash
server {
    listen 443 ssl;
    server_name YOUR_SERVERNAME;
    ssl_certificate /etc/nginx/cert/YOUR_SERVERNAME.crt; 
    ssl_certificate_key /etc/nginx/cert/YOUR_SERVERNAME.key;
    ssl_protocols   TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    charset     utf-8;
    client_max_body_size 75M;   # adjust to taste

    location / {

        uwsgi_pass uwsgi;
        include uwsgi_params;

        # proxy_http_version 1.1;
        # proxy_set_header Host $host;
        # uwsgi_connect_timeout 300s;
        # uwsgi_read_timeout 1800s;
        # uwsgi_send_timeout 300s;
        # uwsgi_buffer_size 256k;
        # uwsgi_buffers 16 256k;
        # uwsgi_busy_buffers_size 512k;
        # uwsgi_temp_file_write_size 512k;

    }

}
```
* 在docker-compose.yml路徑底下運行
```bash
docker-compose up -d
```

## 資料夾結構
---
```
│  .dockerignore
│  .env
│  app.ini
│  Dockerfile
│  requirements.txt
│  run.py
│  wsgi.py
│
├─app
│  │  __init__.py
│  │
│  ├─api
│  │  │  api_test.py
│  │  │
├─nginx
│  │  Dockerfile
│  │  flask_app.conf
│  │  nginx.conf
│  │─cert
│  │  │  DOMAIN.crt
│  │  │  DOMAIN.key
├─nginx_log
│  │  access.log
│  │  error.log
│  │
├─uwsgi_log
│  │  app.log
│  │
```

## 參考資料
---
- [Flask-uWSGI-Nginx-Docker](https://github.com/a607ernie/Flask-uWSGI-Nginx-Docker)
- [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
