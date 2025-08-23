
import configparser

def find_header(file_path, header_name):
    config = configparser.ConfigParser()
    config.read(file_path)

    if header_name in config:
        return dict(config[header_name])
    else:
        return None


madhav = find_header("D:\\Python\\header.ini", "Madhav")
print(madhav)
print(madhav.get('registration_no'))