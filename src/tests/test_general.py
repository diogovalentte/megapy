import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))

from src.megapy import Mega


def test_post(download_url, dest_folder):
    mega = Mega()
    mega.download_url(download_url, dest_folder)
