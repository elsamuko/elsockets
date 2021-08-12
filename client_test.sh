#!/usr/bin/env bash

echo -ne "GET / HTTP/1.1\r
Host: localhost\r
Upgrade: websocket\r
Connection: Upgrade\r
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r
Sec-WebSocket-Protocol: echo\r
Sec-WebSocket-Version: 13\r
\r
" | nc localhost 8765
