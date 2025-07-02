# -*- coding: utf-8 -*-
#
import os

from .conf import ConfigManager

__all__ = [
    'BASE_DIR',
    'PROJECT_DIR',
    'VERSION',
    'CONFIG',
    'MAJOR_VERSION',
    'MINOR_VERSION',
    'PATCH_VERSION',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Version is composed of major, minor and patch numbers
MAJOR_VERSION = 1
MINOR_VERSION = 0
PATCH_VERSION = 0
VERSION = f'{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}'
CONFIG = ConfigManager.load_user_config(root_path=os.path.abspath('/opt/maxkb/conf'))
