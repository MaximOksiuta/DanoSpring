import pandas as pd
from pypdf import PdfReader


def load_data():
    df = pd.read_excel("dataset.xlsx")
    for col in [
        "date_creation",
        "date_inactivation",
        "date_last_updated",
        "date_modify_inner_info",
        "date_publish",
        "date_time_publish",
    ]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def main():
    pd.set_option("display.width", 180)
    pd.set_option("display.max_columns", 100)

    df = load_data()
    _ = "\n".join((page.extract_text() or "") for page in PdfReader("Задание.pdf").pages)

    salary = pd.to_numeric(df["salary"], errors="coerce").where(
        lambda s: (s > 0) & (s < 1_000_000)
    )
    experience = pd.to_numeric(df["experience"], errors="coerce").where(
        lambda s: (s >= 0) & (s <= 60)
    )
    birthday = pd.to_numeric(df["birthday"], errors="coerce")
    age = df["date_publish"].dt.year - birthday
    age = age.where((age >= 14) & (age <= 80))
    region = pd.to_numeric(df["region_code"], errors="coerce").astype("Int64")

    print("shape:", df.shape)
    print("duplicates_all:", int(df.duplicated().sum()))
    print("duplicated_id_cv:", int(df["id_cv"].duplicated().sum()))
    print("duplicated_id_candidate:", int(df["id_candidate"].duplicated().sum()))

    print("\nmissing_top10:")
    print((df.isna().mean() * 100).sort_values(ascending=False).head(10).round(2))

    print("\nsalary_distribution:")
    print(salary.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]).round(2))

    print("\nsalary_by_gender:")
    print(
        pd.DataFrame(
            {
                "count": salary.groupby(df["gender"]).size(),
                "median_salary": salary.groupby(df["gender"]).median(),
                "mean_salary": salary.groupby(df["gender"]).mean(),
            }
        ).round(2)
    )

    print("\nsalary_by_education:")
    print(
        pd.DataFrame(
            {
                "count": salary.groupby(df["education_type"]).size(),
                "median_salary": salary.groupby(df["education_type"]).median(),
                "mean_salary": salary.groupby(df["education_type"]).mean(),
            }
        )
        .sort_values(["median_salary", "count"], ascending=[False, False])
        .round(2)
    )

    print("\nsalary_by_region_min100:")
    region_stats = pd.DataFrame(
        {
            "count": salary.groupby(region).size(),
            "median_salary": salary.groupby(region).median(),
            "mean_salary": salary.groupby(region).mean(),
        }
    )
    print(
        region_stats[region_stats["count"] >= 100]
        .sort_values("median_salary", ascending=False)
        .head(15)
        .round(2)
    )

    print("\nsalary_by_industry_min100:")
    industry_stats = pd.DataFrame(
        {
            "count": salary.groupby(df["industry_code"]).size(),
            "median_salary": salary.groupby(df["industry_code"]).median(),
            "mean_salary": salary.groupby(df["industry_code"]).mean(),
        }
    )
    print(
        industry_stats[industry_stats["count"] >= 100]
        .sort_values("median_salary", ascending=False)
        .head(15)
        .round(2)
    )

    print("\ncorrelations:")
    print("salary~experience:", round(salary.corr(experience), 4))
    print("salary~age:", round(salary.corr(age), 4))


if __name__ == "__main__":
    main()
