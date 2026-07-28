import runpy
from pathlib import Path


PROJECT_APP = Path(__file__).resolve().parents[1] / "Heart-Disease-Prediction" / "frontend" / "streamlit_app.py"

runpy.run_path(str(PROJECT_APP), run_name="__main__")