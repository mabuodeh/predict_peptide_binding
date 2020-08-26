import copy
import pandas as pd


def to_df(pred, count=10):
    """Converts the list of scores to a DataFrame.

    Parameters
    ----------
    pred: list
        Binding prediction list for each query peptide, sorted by binding strength
    count: int
        Number of strongest binding predictions to use

    Returns
    -------
    DataFrame
        binding predictions in DataFrame format
    """

    # SCORE 65.62 PVALUE 0.01766 L 8 N 4
    first_part = ['Score', 'p-value', 'L', 'N']
    columns = copy.deepcopy(first_part)
    residue_count = len(pred[0]) - (len(first_part) * 2)

    for i in range(residue_count):
        columns.append('residue ' + str(i + 1))

    rows = [x for x in range(count)]
    df = pd.DataFrame(columns=columns, index=rows)

    for idx, row in df.iterrows():
        # print(pred[idx])
        # input('')
        row['Score'] = pred[idx][1]
        row['p-value'] = pred[idx][3]
        row['L'] = pred[idx][5]
        row['N'] = pred[idx][7]
        for i in range(1, residue_count + 1):
            # print(i + len(first_part))
            row['residue ' + str(i)] = pred[idx][i + (len(first_part) * 2) - 1]

    return df


def store_in_xlsx(file_name, df, copyright_info):
    """Stores the binding predictions in a excel sheet.

    Parameters
    ----------
    file_name: str
        Name of excel file
    df: DataFrame
        DataFrame containing binding predictions
    copyright_info: list
        Contains copyright information on the original research
    """
    # df = copyright_info.append(df)
    # df.to_excel(file_name)

    writer = pd.ExcelWriter(file_name, engine="xlsxwriter")
    df.to_excel(writer, startcol=0, startrow=7)

    worksheet = writer.sheets['Sheet1']
    for idx, line in enumerate(copyright_info):
        worksheet.write(idx, 0, str(line))

    writer.save()
