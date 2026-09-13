import pandas as pd


def inspect(path_or_url):
    df = pd.read_csv(path_or_url)

    print("Source:", path_or_url)
    print("Shape:", df.shape)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100

    print(pd.DataFrame({
        "Missing Count": missing,
        "Missing Percentage": missing_percent
    }))

    print("\nNumeric summary:")
    print(df.describe())


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
    inspect(url)