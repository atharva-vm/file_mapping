from pathlib import Path


def bank1():
    try:
        location = Path("D:/EFA_NAV/BANK_data/bank1")

        files = {file.name.lower() for file in location.iterdir() if file.is_file()}

        exposure = any("exposure" in file for file in files)
        equity = any("equity" in file for file in files)

        if exposure and equity:
            return True, "Exposure and Equity both available"

        if exposure:
            return False, "Equity file missing"

        if equity:
            return False, "Exposure file missing"

        return False, "Exposure and Equity both missing"

    except Exception as e:
        return False, f"Bank1 Error: {e}"