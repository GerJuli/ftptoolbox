import config

from ftplib import FTP

ftp = FTP(cfg.server)
ftp.login(cfg.user, cfg.password)

open(cfg.local_file_directory+cfg.filename,'rb')                # file to send
ftp.cwd(cfg.remote_file_directory)
ftp.storbinary(cfg.filename, file)                              # send the file
file.close()                                                    # close file and FTP
ftp.quit()


