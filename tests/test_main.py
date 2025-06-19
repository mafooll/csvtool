import subprocess


def test_pipeline_with_subprocess(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "name,price,stock\nAlice,10,yes\nBob,20,no\nCharlie,30,yes\n"
    )

    result = subprocess.run(
        [
            "python",
            "-m",
            "src",
            str(file),
            "--filter",
            "price>10 AND stock=yes",
            "--sort",
            "price:desc",
            "--aggregate",
            "price:avg",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "PRICE:AVG" in result.stdout
    assert "30.0" in result.stdout
