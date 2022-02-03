from pathlib import Path
import os

CODE_PATH = Path(__file__).parent

DATA_FOLDER = Path(__file__).parent / "../data/"

IS_PRODUCTION = os.environ["IS_PRODUCTION"] == "True"