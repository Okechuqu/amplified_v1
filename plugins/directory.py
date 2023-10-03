import os
from typing import List, Dict, Optional


def listdirectory(dir='templates') -> List:
    try:
        if os.path.exists(dir):
            temp = os.listdir(dir)
            container = [(x, str(x).upper()) for x in temp if x != '__init__' ]
            return container
        return []
    except Exception as e:
        return []

