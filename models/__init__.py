#!/usr/bin/python3
"""__init__ the python package file."""

from models.egine.file_storage import FileStorage

storage = FileStorage()
storage.reload()