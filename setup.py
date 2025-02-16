import json
from pathlib import Path
from setuptools import setup

def read_version():
    package_json_path = Path(__file__).resolve().parent / "package.json"
    if not package_json_path.exists():
        raise FileNotFoundError(f"package.json not found at {package_json_path}")
    with package_json_path.open("r", encoding="utf-8") as f:
        return json.load(f)["version"]

setup(
    version=read_version(),
)

