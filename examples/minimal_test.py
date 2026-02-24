import subprocess
import sys


def test_demo_runs():
    r = subprocess.run([sys.executable, "reference-impl/python/demo.py"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "CASE: A_OK" in out
    assert "AUDIT_CARD:" in out
    assert '"gatevector_len": 91' in out


if __name__ == "__main__":
    test_demo_runs()
    print("minimal_test: PASS")
