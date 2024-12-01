import subprocess
from pathlib import Path
import dotenv


def get_version():
    env_version = dotenv.dotenv_values(".env").get("APP_VERSION")
    print(env_version)
    if env_version:
        return env_version

    try:
        # Get version from git tag
        version = (
            subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
        )
        return version
    except:
        # Fallback to reading version file if not in git repo
        try:
            version_file = Path(__file__).parent / ".version"
            return version_file.read_text().strip()
        except:
            return "0.0.0"


__version__ = get_version()