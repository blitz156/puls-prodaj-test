#!/usr/bin/env bash
rsync -ravz --exclude=media . root@5.189.228.198:/root/puls-prodaj-test
ssh root@5.189.228.198 'cd /root/puls-prodaj-test && docker-compose --file docker-compose.production.yml build'
ssh root@5.189.228.198 'cd /root/puls-prodaj-test && docker-compose --file docker-compose.production.yml up -d'