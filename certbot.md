# Request free ssl certificate with certbot

```
sudo apt-get install certbot python3-certbot-nginx
```

```
vim /etc/nginx/nginx.conf
```

```
...
        ssl_protocols TLSv1.2 TLSv1.3;
        server_tokens off;
        server {
           listen 80 http2;
           server_name mta-sts.yourdomain.com;
           return 301 https://mta-sts.yourdomain.com$request_uri; 
        }
        server {
           listen 443 ssl http2; # managed by Certbot
           server_name mta-sts.yourdomain.com;
           ssl_certificate /etc/letsencrypt/live/mta-sts.yourdomain.com/fullchain.pem;
           ssl_certificate_key /etc/letsencrypt/live/mta-sts.yourdomain.com/privkey.pem;
           ssl_trusted_certificate /etc/letsencrypt/live/mta-sts.yourdomain.com/chain.pem;
           location ^~ /.well-known/acme-challenge/ {
               root /usr/share/nginx/html;
               default_type "text/plain";
               try_files $uri =404;
           }
           location = /.well-known/acme-challenge/ {
               return 404;
           }
           location = /.well-known/mta-sts.txt {
           default_type text/plain;
           return 200 "version: STSv1\r\nmode: testing\r\nmx: alt2.aspmx.l.google.com\r\nmx: aspmx.l.google.com\r\nmx: alt3.aspmx.l.google.com\r\nmx: alt4.aspmx.l.google.com\r\nmx: alt1.aspmx.l.google.com\r\nmax_age: 604800\r\n";
           }
           location / {
           limit_except GET HEAD POST { deny all; }
           }
        }
}
...
```

```
service nginx reload
```

```
certbot certonly --webroot -w /usr/share/nginx/html -d mta-sts.yourdomain.com
```

```
service nginx stop

certbot --force-renewal

certbot cnrtonly

certbot renew  --dry-run

certbot nginx start

nginx -s reload
```
