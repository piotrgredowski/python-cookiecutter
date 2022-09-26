import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def handle_vscode_debug_configs():
    add_vscode_debug_configurations = (
        str("{{cookiecutter.add_vscode_debug_configurations}}") == "1"
    )

    if not add_vscode_debug_configurations:
        remove(os.path.join(os.getcwd(), ".vscode"))


def handle_service_and_package_specifics():
    is_service = "{{cookiecutter.service_or_package}}" == "service"

    if not is_service:
        remove(os.path.join(os.getcwd(), "Dockerfile"))
        remove(os.path.join(os.getcwd(), ".dockerignore"))

    is_package = "{{cookiecutter.service_or_package}}" == "package"


HANDLERS = [handle_vscode_debug_configs, handle_service_and_package_specifics]

for handler in HANDLERS:
    handler()
