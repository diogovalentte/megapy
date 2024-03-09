import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))


@pytest.fixture()
def download_url():
    return os.environ.get("DOWNLOAD_URL")


@pytest.fixture()
def dest_folder():
    return os.environ.get("DEST_FOLDER")
