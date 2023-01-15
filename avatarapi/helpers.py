"""
Module for helper functions
"""
import subprocess
from pathlib import Path
from typing import Any

import polars as pl


def get_quotes_df() -> pl.DataFrame:
    """
    Returns the top-level git repo's path
    """

    git_repo = (
        subprocess.Popen(
            ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE
        )
        .communicate()[0]
        .rstrip()
        .decode("utf-8")
    )

    quotes_path = Path(f"{git_repo}/submodules/AvatarQuotes/Quotes.csv")

    return pl.read_csv(quotes_path, sep="|")


# The main quotes dataframe
Quotes = get_quotes_df()


def make_custom_df(column: str, value: str, num: int) -> dict[str, Any]:
    """
    Make a filtered DataFrame for a given column

    column: str
        The name of the column to perform the check on

    value: str
        The value to check the above column against

    num: int
        The number of desired results
    """

    quotes_df = Quotes[Quotes[column] == value]

    if num > (df_len := len(quotes_df)):
        num = df_len

    return quotes_df.sample(n=num).to_dict(False)
