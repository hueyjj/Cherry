import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cherry_dl.core.utils import Config

if __name__ == "__main__":
    import json
    c = Config()
    c.setFormat("mp3")
    print(json.dumps(c.getConfig(), indent=True))
