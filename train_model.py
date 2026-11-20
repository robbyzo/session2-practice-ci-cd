from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    data = pd.read_csv(project_dir / "training_data.csv")

    model = LinearRegression()
    model.fit(data[["YearsExperience"]], data["Salary"])

    joblib.dump(model, project_dir / "linear_model.pkl")
    (project_dir / "linear_model.txt").write_text(
        f"Coefficients: {model.coef_}\nIntercept: {model.intercept_}\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
