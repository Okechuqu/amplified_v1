
import os
from typing import List
from decouple import config


def webDirectory() -> List:
    try:
        # declare an empty container
        container = []
        path_to_dir = os.path.abspath(config('WEBSITE_DIR'))

        if os.path.exists(path_to_dir):
            #
            directory = os.listdir(path_to_dir)
            #
            for x in directory:

                # if condition prevents importing default template.
                # which starts with a name _ or __
                if not str(x).startswith('_') or str(x).startswith('__'):
                    directories = os.path.abspath(
                        f"{config('WEBSITE_DIR')}/{x}")
                    container.append(str(directories))
        return container
    except Exception as e:
        return e
