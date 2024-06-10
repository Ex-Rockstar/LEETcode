import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    employees['bonus'] = 2*employees['salary']
    df = pd.DataFrame(employees)

    return df    