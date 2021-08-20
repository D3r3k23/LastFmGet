venv/bin/activate
pip install -qqq LastFmApi
python test/tests.py
pip uninstall -qqq -y LastFmApi
deactivate
