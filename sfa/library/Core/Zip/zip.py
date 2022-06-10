import zipfile
def unzip(zip_file_path,pwd,target_path):
    zip_file = zipfile.ZipFile(zip_file_path)
    zip_list = zip_file.namelist()

    for f in zip_list:
        zip_file.extract(f,target_path,pwd.encode("utf-8"))
    zip_file.close()
