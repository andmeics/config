# Request free ssl certificate with certbot

```
sudo apt-get install certbot python3-certbot-nginx
```

```
vim /etc/nginx/nginx.conf
```

```
...
        server {
           server_name mta-sts.yourdomain.com;
           listen 443 ssl; # managed by Certbot
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
