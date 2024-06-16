#!/usr/bin/env python3

#
# author : Michael Gene Brockus - (Dreamer)
# contact: <mailto:michaelbrockus@gmail.com>
# license: Mozilla Public License 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2024 The Fossil Logic development team
#
from .authorinfo import ProjectAuthor
from .projectinfo import ProjectInfo
import typing as T
import sys

error_message: T.AnyStr = """ERROR: Tried to install Wrap-ui with Python version: {0}

WrapDB-ui requires Python 3.6.0 or greater
"""


class PackageInfo(ProjectAuthor, ProjectInfo):
    def __init__(self):
        super().__init__()
        self.required_version()

    @staticmethod
    def long_description():
        return "WrapDB-ui is a client GUI for Meson build WrapDB system."

    @staticmethod
    def required_version() -> None:
        if sys.version_info < (3, 6, 0):
            raise SystemExit(error_message.format(sys.version))

    @staticmethod
    def get_data_files() -> T.List:
        data_files: T.List = []
        if sys.platform != "win32":
            # Only useful on UNIX-like systems
            data_files = [("share/man/man1", ["man/meson-ui.1"])]
        return data_files
