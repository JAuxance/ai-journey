import numpy as np
import pandas as pd


LINE_WIDTH = 68


def page_title(title):
    print("\n" + "=" * LINE_WIDTH)
    print(title.upper().center(LINE_WIDTH))
    print("=" * LINE_WIDTH)


def section(title):
    print(f"\n[ {title} ]")
    print("-" * LINE_WIDTH)


def show_df(name, df):
    print(f"{name} -> shape={df.shape}, dtypes below")
    print(df)


# Pandas topic:
# - Series: the 1D labeled array at the core of pandas
def series_section():
    section("1. Series")

    s = pd.Series([1, 3, 5, np.nan, 6, 8])

    print(f"pd.Series([1, 3, 5, nan, 6, 8]) ->\n{s}")
    print(f"dtype -> {s.dtype}")
    print(f"I see that NaN forces the dtype to float64 -> {s.dtype == np.float64}")


# Pandas topics:
# - Creating a DataFrame from a NumPy array with a DatetimeIndex
# - Creating a DataFrame from a dict with mixed types
def dataframe_creation_section():
    section("2. DataFrame Creation")

    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )

    show_df("df (randn + DatetimeIndex)", df)
    print()
    show_df("df2 (mixed types)", df2)
    print(f"\ndf2 dtypes ->\n{df2.dtypes}")
    print(f"\nI see that each column can have its own dtype -> {df2.dtypes.nunique() > 1}")


# Pandas topics:
# - Viewing the top and bottom rows
# - Accessing index and columns
# - Converting to a NumPy array
def viewing_section():
    section("3. Viewing Data")

    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    print(f"df.head() ->\n{df.head()}")
    print(f"\ndf.tail(3) ->\n{df.tail(3)}")
    print(f"\ndf.index ->\n{df.index}")
    print(f"\ndf.columns ->\n{df.columns}")
    print(f"\ndf.to_numpy() ->\n{df.to_numpy()}")
    print(f"\nI see that to_numpy() loses the labels -> {type(df.to_numpy()).__name__}")


# Pandas topics:
# - Creating a DataFrame from a dict with a custom string index
# - Adding rows with concat
def custom_index_section():
    section("4. Custom Index And Concat")

    data = {
        "Type": ["MOBA", "Sandbox", "Sandbox"],
        "Authors": ["Brandon Beck", "Markus Persson", "N/A"],
        "Studio": ["Riot Games", "Microsoft", "Pugstorm"],
    }
    df3 = pd.DataFrame(data, index=["League of Legends", "Minecraft", "CoreKeeper"])

    new_row = pd.DataFrame(
        [{"Type": "Battle Royal", "Authors": "Tim Sweeney", "Studio": "Epic Games"}],
        index=["Fortnite"],
    )
    df3 = pd.concat([df3, new_row])

    show_df("df3 (games)", df3)
    print(f"\nI see that strings work as index and concat adds rows -> {len(df3)} rows total")


# Pandas topics:
# - Reading a CSV file with a custom index column
# - Reading a JSON file
# - Selecting a specific row and columns with loc
def read_csv_json_section():
    section("5. Reading CSV And JSON")

    df_csv = pd.read_csv("../matplotlib/data/pokemon.csv", index_col="Name")
    df_json = pd.read_json("data/pokemon.json")

    show_df("pd.read_csv(pokemon.csv)", df_csv)
    print()
    show_df("pd.read_json(pokemon.json)", df_json)
    print(f"\ndf_csv.loc[\"Pikachu\", [\"Type 1\", \"Speed\"]] ->\n{df_csv.loc['Pikachu', ['Type 1', 'Speed']]}")
    print(f"\nI see that loc uses the index label, not a row number -> {df_csv.index.name}")


# Pandas topics:
# - Aggregations on the whole DataFrame (mean, sum)
# - Aggregations on a single column
# - Grouping rows by a category with groupby
def operations_section():
    section("6. Operations And GroupBy")

    df = pd.read_csv("../matplotlib/data/pokemon.csv", index_col="Name")

    print(f"df.mean(numeric_only=True) ->\n{df.mean(numeric_only=True)}")
    print(f"\ndf.sum(numeric_only=True) ->\n{df.sum(numeric_only=True)}")

    print(f"\ndf[\"Speed\"].mean()  -> {df['Speed'].mean()}")
    print(f"df[\"HP\"].mean()     -> {df['HP'].mean()}")
    print(f"df[\"Attack\"].max()  -> {df['Attack'].max()}")

    group = df.groupby("Type 1")
    print(f"\ngroup[\"Attack\"].mean() ->\n{group['Attack'].mean()}")
    print(f"\ngroup[\"Speed\"].max() ->\n{group[['Speed']].max()}")
    print(f"\ngroup[\"Defense\"].max() ->\n{group[['Defense']].max()}")
    print(f"\ngroup[\"Total\"].min() ->\n{group[['Total']].min()}")
    print(f"\nI see that groupby splits the DataFrame by category for aggregation")


# Pandas topics:
# - Dropping columns
# - Filling missing values with fillna
# - Replacing inconsistent values with replace
def data_cleaning_section():
    section("7. Data Cleaning")

    df = pd.read_csv("../matplotlib/data/pokemon.csv", index_col="Name")

    df = df.drop(columns=["Legendary", "#"])
    print(f"After drop(columns=[\"Legendary\", \"#\"]) -> {list(df.columns)}")

    df = df.dropna(subset=["Type 2"])
    print(f"\ndf.dropna(subset=[\"Type 2\"]) ->\n{df['Type 2']}")

    df["Type 1"] = df["Type 1"].replace({
        "Grass":    "Terre",
        "Fire":     "Feu",
        "Water":    "Eau",
        "Fairy":    "Fée",
        "Fighting": "Combat",
        "Flying":   "Vol",
    })
    print(f"\nType 1 after replace (sample) ->\n{df['Type 1'].value_counts().head(8)}")
    print(f"\nI see that replace lets you fix inconsistent values without a loop")

def manipulation_section():
    section("8. Manipulation")

    rng = np.random.default_rng(42)
    df = pd.DataFrame(rng.choice(30, size=5, replace=False))

    data = {
        "Game": ["League of Legends", "Minecraft", "CoreKeeper"],
        "Type": ["MOBA", "Sandbox", "Sandbox"],
        "Authors": ["Brandon Beck", "Markus Persson", "N/A"],
        "Studio": ["Riot Games", "Microsoft", "Pugstorm"],
    }
    df1 = pd.DataFrame(data, index=["League of Legends", "Minecraft", "CoreKeeper"])

    print(f"df (random values) ->\n{df}\n")
    print(f"df.iloc[2] (by position) ->\n{df1.iloc[2]}\n")
    print(f"df.loc[:, \"Type\"] (by label) ->\n{df1.loc[:, 'Type']}\n")

    print(f"df[df >= 15] (boolean filter) ->\n{df[df >= 15]}\n")

    df3 = df[df % 2 == 0]
    df3 = df3.fillna(0)
    print(f"df[df % 2 == 0].fillna(0) ->\n{df3}")


def df_info_section():
    section("9. DataFrame Info")

    poke_df = pd.read_csv("../matplotlib/data/pokemon.csv", index_col="Name")

    print("\npoke_df.info() ->")
    poke_df.info()
    print(f"\npoke_df.describe() ->\n{poke_df.describe()}")

def sort_section():
    section("10. Sorting Data")

    rng = np.random.default_rng(42)

    df = pd.DataFrame(rng.integers(-40, 50, size=(5, 3)), columns=list("ABC"))
    df1 = df.sort_values(by=list("A"), ascending=False).reset_index(drop=True)

    print(f"\nOriginal DataFrame ->\n{df}\n")
    print(f"sort_values(by=\"A\", ascending=False).reset_index(drop=True) ->\n{df1}\n")

    df["A*B"] = df["A"] * df["B"]
    print(f"df with new column A*B ->\n{df}")

def encoding_section():
    section("11. Encoding Categorical Data")

    data = {
        "gender": ["male", "female", "female", "male"],
        "lunch": ["standard", "free/reduced", "standard", "free/reduced"],
        "score": [72, 85, 90, 68]
    }

    df = pd.DataFrame(data)

    df_encoded = pd.get_dummies(df, columns=["gender", "lunch"])

    print(f"original DataFrame ->\n{df}")
    print(f"df_encoded DataFrame ->\n{df_encoded}")
    print(f"df_encoded.dtypes() ->\n{df_encoded.dtypes}")

def main():
    page_title("My Pandas Journal")
    series_section()
    dataframe_creation_section()
    viewing_section()
    custom_index_section()
    read_csv_json_section()
    operations_section()
    data_cleaning_section()
    manipulation_section()
    df_info_section()
    sort_section()
    encoding_section()


if __name__ == "__main__":
    main()
