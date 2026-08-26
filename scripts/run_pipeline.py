from extract import extract
from load import load_latest_raw_to_sql
from transform import transform


def run_pipeline():

    print("=" * 50)
    print("CRYPTO MARKET PIPELINE")
    print("=" * 50)

    try:

        print("\n[1/3] Extracting data...")
        extract()
        print("✓ Extraction complete")

        print("\n[2/3] Loading data...")
        load_latest_raw_to_sql()
        print("✓ Loading complete")

        print("\n[3/3] Transforming data...")
        transform()
        print("✓ Transformation complete")

        print("\n" + "=" * 50)
        print("PIPELINE COMPLETE")
        print("=" * 50)

    except Exception as error:

        print("\n" + "=" * 50)
        print("PIPELINE FAILED")
        print("=" * 50)

        print(f"\nError: {error}")

        raise

if __name__ == "__main__":
    run_pipeline()