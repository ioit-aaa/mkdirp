import os
from pathlib import Path


def mkdirp(path, mode=0o777):
    path = Path(path).resolve()
    
    if path.exists():
        if not path.is_dir():
            raise FileExistsError(f"{path} exists and is not a directory")
        return str(path)
    
    try:
        path.mkdir(parents=True, mode=mode, exist_ok=True)
    except Exception as e:
        raise OSError(f"Failed to create {path}: {e}")
    
    return str(path)