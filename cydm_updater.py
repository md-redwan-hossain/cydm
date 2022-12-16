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
        self.mismatched_hash = False
        self.mismatched_file_count = False

        self.cydm_files: list = []
        self.cydm_files_ignored: list = ["trial.py", "failed_download.log"]

        for file in os.listdir(self.BASE_DIR):
            if os.path.isdir(f"{self.BASE_DIR}/{file}"):
                self.cydm_files_ignored.append(file)

        for file in os.listdir(self.BASE_DIR):
            if file not in self.cydm_files_ignored:
                self.cydm_files.append(file)

        self.cydm_files = sorted(self.cydm_files)


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


class RepoManagement(DirectoryManagement):
    def clone_repo(self):
        print(colored.yellow("\n\nDownloading repo"))
        git.Repo.clone_from(
            "https://github.com/redwan-hossain/cydm.git",
            f"{self.BASE_DIR}/new_files", branch='main', depth="1")
        print(colored.yellow("Download finished\n"))


class FileManagement(RepoManagement):
    def copy_old(self):
        for i in self.cydm_files:
            shutil.copy(f"{self.BASE_DIR}/{i}",
                        f"{self.BASE_DIR}/old_files/{i}")

    def update_new_file_list(self):
        for file in os.listdir(f"{self.BASE_DIR}/new_files"):
            if os.path.isfile(f"{self.BASE_DIR}/new_files/{file}"):
                self.files_new.append(file)

        self.files_new = sorted(self.files_new)

    def check_file_amount_mismatch(self):
        if len(self.cydm_files) != len(self.files_new):
            return True
        else:
            return False


class HashingManagement(FileManagement):
    def hash_maker(self, file_name):
        with open(f"{file_name}", "rb") as file:
            md5Hash_current = hashlib.md5(file.read())
            hex = md5Hash_current.hexdigest()
            return hex

    def hash_manager_old(self):
        for i in self.cydm_files:
            hex = self.hash_maker(f"{self.BASE_DIR}/old_files/{i}")
            self.hash_old[i] = f"{hex}"

    def hash_manager_new(self):
        for i in self.files_new:
            hex = self.hash_maker(f"{self.BASE_DIR}/new_files/{i}")
            self.hash_new[i] = f"{hex}"


class HashingCompare(HashingManagement):

    def compare_hash_for_mismatch(self):
        for file_name, hex in self.hash_old.items():
            if self.hash_new.get(file_name) != hex:
                return True


class UpdateCYDM(HashingCompare):
    def remove_current_files(self):
        for i in self.cydm_files:
            os.remove(f"{self.BASE_DIR}/{i}")

    def update_from_new_files(self):
        for i in self.cydm_files:
            shutil.copy(f"{self.BASE_DIR}/new_files/{i}",
                        f"{self.BASE_DIR}/{i}")


def run_update_check() -> bool:
    update_obj = UpdateCYDM()
    update_obj.manage_directory()
    update_obj.copy_old()
    update_obj.clone_repo()
    update_obj.update_new_file_list()
    update_obj.mismatched_file_count = update_obj.check_file_amount_mismatch()

    if update_obj.mismatched_file_count:
        perform_update(update_obj)
    else:
        run_hash_check(update_obj)

    if update_obj.mismatched_file_count or update_obj.mismatched_hash:
        return True
    else:
        return False


def run_hash_check(update_obj):
    update_obj.hash_manager_old()
    update_obj.hash_manager_new()
    update_obj.mismatched_hash = update_obj.compare_hash_for_mismatch()

    if update_obj.mismatched_hash:
        perform_update(update_obj)
    else:
        update_obj.manage_directory()


def perform_update(update_obj):
    update_obj.remove_current_files()
    update_obj.update_from_new_files()
    update_obj.manage_directory()
