from typing import Any, Type

import pandas as pd
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session
from tqdm import tqdm

from utils import batch, nan_to_null


def turn_all_query_to_df(query:Query):
    return pd.DataFrame(query, columns=[x["name"] for x in query.column_descriptions] )

def bulk_add_list(s:Session, insertion_list:pd.DataFrame, model:Type[DeclarativeMeta] = None, batch_size = 1000,
                  handle_existing="ignore", created_by: str = None):
    """
    this implement an upsert and

    """
    if len(insertion_list)>0:
        print("remember to commit your session afterwards")
        assert isinstance(insertion_list, pd.DataFrame)
        if created_by is not None:
            insertion_list["created_by"] = created_by
        columns = insertion_list.columns
        assert isinstance(model, DeclarativeMeta), "model has to be a sql model"
        assert handle_existing in ["ignore", "update", None]

        insertion_list = nan_to_null(insertion_list)

        insertion_list = insertion_list.to_dict("records")
        print(f"insertion records of the form: {insertion_list[0]}")
        print(len(insertion_list))
        #each element in the list is a thing that can be aded to the db
        for elem in tqdm(batch(insertion_list, batch_size), total=int(len(insertion_list) / batch_size)):
            stmt = insert(model).values(elem)
            if handle_existing == "ignore":
                stmt = stmt.on_conflict_do_nothing()

            if handle_existing == "update":
                # define dict of non-primary keys for updating
                # get list of fields making up primary key
                primary_keys = [key.name for key in inspect(model).primary_key]
                update_dict = {
                    c.name: c
                    for c in stmt.excluded
                    if ((not c.primary_key) and (c.name in columns))  # added fact it is in dataframe
                }
                # cover case when all columns in table comprise a primary key
                # in which case, upsert is identical to 'on conflict do nothing.
                if update_dict == {}:
                    print("only supplying primary key, has to e handled differently")
                    return None
                # assemble new statement with 'on conflict do update' clause
                stmt = stmt.on_conflict_do_update(
                    index_elements=primary_keys,
                    set_=update_dict,
                )

            s.execute(stmt)

    else:
        print(f"WARNING: Empty Record Update, now Rows updated ")

def bulk_update_list(s:Session, insertion_list:pd.DataFrame, model:Type[Any], batch_size = 1000):

    #each element in the list is a thing that can be aded to the db
    print("remember to commit your session afterwards")
    insertion_list = nan_to_null(insertion_list)
    insertion_list = insertion_list.to_dict("records")

    if len(insertion_list)>0:
        print(f"example record: {insertion_list[0]}")
        for elem in tqdm(batch(insertion_list, batch_size), total=int(len(insertion_list) / batch_size)):
            s.bulk_update_mappings(model, elem)
    else:
        print(f"WARNING: Empty Record Update, now Rows updated ")


