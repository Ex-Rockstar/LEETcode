import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:

    df = pd.DataFrame(customers)
    return df.drop_duplicates('email')
     
    
    