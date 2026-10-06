"""Regression checks for image loading and red-buoy detection."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PROGRAM = Path(sys.argv[1]).resolve()


def run_sample(name):
    result = subprocess.run(
        [str(PROGRAM), str(ROOT / "samples" / name)],
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
    return dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line)


for name in (
    "buoy_left.jpg",
    "buoy_center.jpg",
    "buoy_right.jpg",
    "buoy_near_left.jpg",
    "buoy_near_right.jpg",
    "buoy_tolerance_left.jpg",
    "buoy_tolerance_right.jpg",
    "buoy_partial_left.jpg",
    "buoy_partial_right.jpg",
):
    output = run_sample(name)
    assert output["status"] == "FOUND", (name, output)
    assert int(output["buoy_width"]) > 40, (name, output)

assert run_sample("no_buoy.jpg")["status"] == "NOT_FOUND"
print("Provided image loading and buoy detection: 10 samples passed")
