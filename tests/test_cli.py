import subprocess

def test_cleartrack_runs():
    result = subprocess.run(["python3", "cleartrack/cli.py", "--stats"], capture_output=True, text=True)
    assert "You have cleared your terminal" in result.stdout