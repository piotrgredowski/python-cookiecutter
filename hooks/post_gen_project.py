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


HANDLERS = [handle_vscode_debug_configs]

for handler in HANDLERS:
    handler()
