from clint.textui import colored
import hashlib
import shutil
import os
import git


class ResourceManagement:
    def __init__(self) -> None:
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.files_new: list = []
        self.hash_old: dict = {}
        self.hash_new: dict = {}
        self.cydm_files: list = [
            'LICENSE', 'cydm.py', 'download_preference.py', 'exception_handler_core.py', 'exception_handler_helper.py', 'playlist_core.py', 'regex_link_validation.py', 'requirements.txt', 'selection_validation.py', 'time_converter.py', 'updater.py', 'video_core.py']


class DirectoryManagement(ResourceManagement):
    def manage_directory(self):
        if os.path.exists(f"{self.BASE_DIR}/old_files"):
            shutil.rmtree(f"{self.BASE_DIR}/old_files")
        else:
            os.mkdir(f"{self.BASE_DIR}/old_files")

        if os.path.exists(f"{self.BASE_DIR}/new_files"):
            shutil.rmtree(f"{self.BASE_DIR}/new_files")
        else:
            os.mkdir(f"{self.BASE_DIR}/new_files")


class FileManagement(DirectoryManagement):
    def copy_old(self):
        for i in self.cydm_files:
            shutil.copy(f"{self.BASE_DIR}/{i}",
                        f"{self.BASE_DIR}/old_files/{i}")

    def clean_unnecessary_files(self):
        self.files_new = sorted(os.listdir(f"{self.BASE_DIR}/new_files"))

        for i in self.files_new:
            if i not in self.cydm_files:
                try:
                    os.remove(f"{self.BASE_DIR}/new_files/{i}")
                except IsADirectoryError:
                    shutil.rmtree(f"{self.BASE_DIR}/new_files/{i}")

        self.files_new.clear()
        self.files_new = sorted(os.listdir(f"{self.BASE_DIR}/new_files"))


class RepoManagement(FileManagement):
    def clone_repo(self):
        print(colored.yellow("\n\nDownloading repo"))
        git.Repo.clone_from(
            "https://github.com/redwan-hossain/cydm.git", f"{self.BASE_DIR}/new_files", branch='main', depth="1")
        print(colored.yellow("Download finished\n"))
        self.clean_unnecessary_files()


class HashingManagement(RepoManagement):
    def hash_maker(self, file_name):
        with open(f"{file_name}", "rb") as file:
            md5Hash_current = hashlib.md5(file.read())
            hex = md5Hash_current.hexdigest()
            return hex

    def hash_manager_old(self):
        for i in self.cydm_files:
            hex = self.hash_maker(f"{self.BASE_DIR}/{i}")
            self.hash_old[i] = f"{hex}"

    def hash_manager_new(self):
        for i in self.files_new:
            hex = self.hash_maker(f"{self.BASE_DIR}/new_files/{i}")
            self.hash_new[i] = f"{hex}"


class HashingCompare(HashingManagement):

    def compare_hash(self):
        for file_name, hex in self.hash_old.items():
            if self.hash_new.get(file_name) != hex:
                return False


class UpdateCYDM(HashingCompare):
    def remove_current_files(self):
        for i in self.cydm_files:
            os.remove(f"{self.BASE_DIR}/{i}")

    def update_from_new_files(self):
        for i in self.cydm_files:
            shutil.copy(f"{self.BASE_DIR}/new_files/{i}",
                        f"{self.BASE_DIR}/{i}")


def run_update_check():
    update_obj = UpdateCYDM()
    update_obj.manage_directory()
    update_obj.copy_old()
    update_obj.clean_unnecessary_files()
    update_obj.clone_repo()
    update_obj.hash_manager_old()
    update_obj.hash_manager_new()
    result = update_obj.compare_hash()
    if result == False:
        update_obj.remove_current_files()
        update_obj.update_from_new_files()
        update_obj.manage_directory()
        return True
    else:
        update_obj.manage_directory()
        return False
