# Session 2 Practice · CI/CD with GitHub Actions

This exercise trains a linear regression model to predict salary from years of experience. It writes the trained model to `linear_model.pkl` and the coefficient and intercept to `linear_model.txt`.

## Run locally

```bash
python -m pip install -r requirements.txt
python train_model.py
```

## Run on GitHub

Change `training_data.csv` and open a pull request to `main` to check that the model trains. When the data change reaches `main`, the workflow trains the model, commits `linear_model.txt` to the `release` branch, and publishes a versioned GitHub Release containing the same file. The `release` branch is created automatically on the first publication.
