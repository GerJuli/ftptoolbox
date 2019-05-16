import config as cfg

from ftplib import FTP

ftp = FTP(cfg.server)
ftp.login(cfg.ftp_credentials['user'], cfg.ftp_credentials['password'])
try:
    file = open(cfg.local_file_directory+cfg.filename,'rb')                # file to send
except FileNotFoundError:
    print("Local file not found. Check config!")
try:
    ftp.cwd(cfg.remote_file_directory)
except:
    print("Remote directory not found. Check config")
ftp.storbinary("STOR "+cfg.filename, file) 
file.close()                                                    # close file and FTP
ftp.quit()


