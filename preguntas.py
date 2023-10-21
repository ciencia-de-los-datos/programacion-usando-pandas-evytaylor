"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]


def pregunta_02():
    return tbl0.shape[1]


def pregunta_03():
    gp0 = tbl0.groupby("_c1")["_c1"].count()

    return gp0



def pregunta_04():

    gp1 = tbl0.groupby("_c1")["_c2"].mean()

    return gp1



def pregunta_05():
    gp2 = tbl0.groupby("_c1")["_c2"].max()

    return gp2


def pregunta_06():
    list0 = sorted(list(tbl1["_c4"].unique()))
    list0 = [x.upper() for x in list0]

    return list0



def pregunta_07():
    gp3 = tbl0.groupby("_c1")["_c2"].sum()

    return gp3


def pregunta_08():
    gp4 = tbl0.copy()
    gp4["suma"] = gp4["_c0"] + gp4["_c2"]

    return gp4



def pregunta_09():
    gp5 = tbl0.copy()
    gp5["year"] = gp5["_c3"].str[:4]

    return gp5



def pregunta_10():
    gp6 = tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(map(str,sorted(list(x)))))
    new_df = pd.DataFrame(gp6)

    return new_df

def pregunta_11():
    gp7 = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(map(str,sorted(list(x))))).reset_index()

    return gp7


def pregunta_12():
    tbl2["_c5"] = tbl2["_c5a"].astype(str) + ":" + tbl2["_c5b"].astype(str)
    gp8 = tbl2.groupby("_c0")["_c5"].apply(lambda x: ",".join(sorted(list(x)))).reset_index()
    new_df1 = pd.DataFrame(gp8)

    return new_df1



def pregunta_13():
    tbl0.set_index("_c0")
    tbl2.set_index("_c0")

    comb = pd.merge(tbl0,tbl2,on="_c0")
    gp9 = comb.groupby("_c1")["_c5b"].sum()

    return gp9
