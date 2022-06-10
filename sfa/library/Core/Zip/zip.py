import zipfile
from zipfile import ZipFile
def unzip(zip_file_path,pwd,target_path):
    zip_file = support_gbk(zipfile.ZipFile(zip_file_path))
    zip_list = zip_file.namelist()

    for f in zip_list:
        zip_file.extract(f,target_path,pwd.encode("utf-8"))
    zip_file.close()



def support_gbk(zip_file: ZipFile):
    name_to_info = zip_file.NameToInfo
    # copy map first
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file

