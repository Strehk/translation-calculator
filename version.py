
import subprocess
from pathlib import Path

def get_version():
    try:
        # Get version from git tag
        version = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
        return version
    except:
        # Fallback to reading version file if not in git repo
        try:
            version_file = Path(__file__).parent / '.version'
            return version_file.read_text().strip()
        except:
            return "0.0.0"

__version__ = get_version()