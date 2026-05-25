#!/bin/bash
#State → current connection status
#Local Address → your machine’s IP address and port
#Remote Address → destination IP address and port
#Process → program/process using the connection
ss -tunp | column -t

