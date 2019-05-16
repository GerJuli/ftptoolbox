import config

from ftplib import FTP

ftp = FTP(cfg.server)
ftp.login(cfg.user, cfg.password)
