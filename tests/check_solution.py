"""Regression checks for geometry and relative-position calculations."""

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


for name, expected_position in (
    ("buoy_left.jpg", "LEFT"),
    ("buoy_center.jpg", "CENTER"),
    ("buoy_right.jpg", "RIGHT"),
    ("buoy_near_left.jpg", "LEFT"),
    ("buoy_near_right.jpg", "RIGHT"),
    ("buoy_tolerance_left.jpg", "CENTER"),
    ("buoy_tolerance_right.jpg", "CENTER"),
    ("buoy_partial_left.jpg", "LEFT"),
    ("buoy_partial_right.jpg", "RIGHT"),
):
    output = run_sample(name)
    assert output["position"] == expected_position, (name, output)
    center = int(output["buoy_x"]) + int(output["buoy_width"]) // 2
    assert int(output["buoy_center_x"]) == center, (name, output)
    assert int(output["offset_px"]) == center - int(output["image_width"]) // 2, (
        name,
        output,
    )

assert run_sample("no_buoy.jpg")["status"] == "NOT_FOUND"
print("Geometry and position logic: 10 samples passed")
