import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL to fetch JSON data
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.json?accessType=DOWNLOAD"

response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON

    # Extract column names from metadata (if available)
    if "meta" in data and "view" in data["meta"] and "columns" in data["meta"]["view"]:
        column_names = [col['name'] for col in data['meta']['view']['columns']]
    else:
        print("Could not find column names in metadata.")
        column_names = None

    # Extract the dataset (check if 'data' key exists and is not empty)
    if 'data' in data and len(data["data"]) > 0:
        df = pd.DataFrame(data["data"])  # Load the data first

        # Assign column names if available and match the number of columns
        if column_names and len(column_names) == df.shape[1]:
            df.columns = column_names
        else:
            print("Column names do not match data structure.")
    else:
        print("No actual data found in the API response.")
        df = pd.DataFrame()  # Create an empty DataFrame to avoid further errors

    # Extract "averageRating" separately from metadata (not part of DataFrame)
    average_rating = data.get("meta", {}).get("view", {}).get("averageRating", None)
    print("Dataset Average Rating:", average_rating)

    # Proceed only if the DataFrame is not empty
    if not df.empty:
        # Print available column names
        print("Available Columns:", df.columns.tolist())

        # Drop unwanted columns if they exist
        columns_to_drop = ["Row ID", "Some Unwanted Column"]  # Modify based on actual data
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors="ignore")

        # Convert numeric columns (adjust based on actual column names)
        numeric_columns = ["Model Year", "Electric Range", "Base MSRP"]  # Adjust accordingly
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Drop columns where more than 50% of values are missing instead of dropping rows
        df = df.dropna(thresh=len(df) * 0.5, axis=1)  # Drop columns with >50% NaNs

        # Display DataFrame structure
        print(df.info())

        # Display first few rows
        print(df.head())


if "Make" in df.columns:
    df["Make"].value_counts().nlargest(10).plot(kind="bar", color="skyblue", edgecolor="black")
    plt.xlabel("Vehicle Make")
    plt.ylabel("Number of Vehicles")
    plt.title("Top 10 Most Common Electric Vehicle Makes")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Column 'Make' not found in dataset.")
import seaborn as sns

if "Make" in df.columns and "Electric Range" in df.columns:
    plt.figure(figsize=(14,6))
    df_filtered = df[df["Electric Range"].notna()]  # Remove NaN values
    df_filtered["Electric Range"] = pd.to_numeric(df_filtered["Electric Range"], errors="coerce")  # Ensure numeric type

    # Select top 10 most common makes for readability
    top_makes = df_filtered["Make"].value_counts().nlargest(10).index
    df_filtered = df_filtered[df_filtered["Make"].isin(top_makes)]

    sns.boxplot(x="Make", y="Electric Range", data=df_filtered)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Vehicle Make")
    plt.ylabel("Electric Range (Miles)")
    plt.title("Electric Range Distribution by Vehicle Make (Top 10)")
    plt.show()
else:
    print("Required columns ('Make', 'Electric Range') not found.")

