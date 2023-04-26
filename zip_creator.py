import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed_zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, archname=filepath.name)

