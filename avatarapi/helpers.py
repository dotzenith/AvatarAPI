"""
Module for helper functions
"""
import subprocess
from pathlib import Path

import pandas as pd


def get_quotes_file() -> Path:
    """
    Returns the top-level git repo's path
    """
    
    git_repo = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], 
                                 stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    
    return Path(f"{git_repo}/submodules/AvatarQuotes/Quotes.csv")

# Avoiding circular import
from avatarapi.models import Quotes


def make_dataframe(column: str, value: str, num: int) -> pd.DataFrame:
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

    if num > (df_len := len(quotes_df.index)):
        num = df_len

    return quotes_df.sample(n=num).to_dict("records")
