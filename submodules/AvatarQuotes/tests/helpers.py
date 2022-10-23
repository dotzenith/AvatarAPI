"""
A few helper functions for tests and compiling a big csv file from all of the smaller ones
"""

import pandas as pd
from pathlib import Path
import subprocess

def main():
    """
    The driver function to output a newly complied csv
    """
    quotes_df = make_dataframe()
    output_csv(quotes_df)

def get_git_repo() -> str:
    """
    Returns the top-level git repo's path
    """
    
    return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], 
                                 stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')

def make_dataframe() -> pd.DataFrame:
    """
    Makes a DataFrame from all of the CSV files from all seasons
    """
   
    git_path = get_git_repo()
    sub_dirs = [f"{git_path}/books/01_Water", f"{git_path}/books/02_Earth", f"{git_path}/books/03_Fire"]

    dfs = []
    for sub_dir in sub_dirs:
        files = Path(sub_dir).glob("*.csv")
        for file in files:
            dfs.append(pd.read_csv(file, sep="|"))

    return pd.concat(dfs)

def output_csv(dataframe: pd.DataFrame) -> None:
    """
    A simple wrapper to output a given dataframe to csv
    """
   
    git_repo = get_git_repo()
    dataframe.to_csv(f"{git_repo}/Quotes.csv", sep="|", index=False)

if __name__ == "__main__":
    main()
