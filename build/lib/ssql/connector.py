#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Handling SQL Connection with the server.
    
Created on Tue Dec 9 15:27:19 2021

@author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com

Copyright (C) Ujjawal K. Panchal - All Rights Reserved.
Unauthorized copying of this file, via any medium is strictly prohibited.
Proprietary and confidential.
"""

#importing libraries.
from typing import Optional, Iterable, Union
import mysql.connector
import pickle

fallacy_list = ["insert", "update", "alter"]

def list_in_str(l, query):
    """
    if an element of the list is in query raise exception <!>
    """
    for ele in l:
        if ele in query:
            return True
    return False

def query_constraint(query: str, parameters: Union[Iterable, dict]):
    """
    To stop user from doing something potentially dangerous in db. For eg. it is not safe to: `select * from <a huge table>;`. 
    """
    if list_in_str(fallacy_list, query.lower()) or ( ("select" in query.lower()) and ("limit" not in query.lower()) ):
        raise Exception(f"Query Unpassable <!> : {query}. Please donot use insert, update,"
                        "alter in query and always use limit.")
    return query, parameters

class Connection():
    """
    Class to handle connection with the server.
    ===
    creds: Either an iterable or a string.
    poolsize (optional, default = 3): size of the cx pool.
    poolname (optional, default = 'mypool'): name of the cx pool.
    """
    def __init__(self, creds: Union[Iterable, str], poolsize: int = 3, poolname: str = "mypool"):
        self.sql_creds = self.get_creds(creds)
        self.poolname = poolname
        self.poolsize = poolsize
        self.connect()
        return

    def get_creds(self, creds: Union[Iterable, str, None] = None):
        assert creds, f"Need creds for connection."
        cols = ["user", "password", "host", "db"]
        sql_creds = {}

        if isinstance(creds, str): #if its a file parse it to variable.
            with open(creds, "rb") as f:
                creds = pickle.load(f)
        
        #process variables.
        if isinstance(creds, Iterable) and not isinstance(creds, dict):
            assert len(creds) == 4, f"Invalid Credentials."
            for i, val in enumerate(creds):
                sql_creds[cols[i]] = val
        elif isinstance(creds, dict):
            cols = ["host", "db", "user", "password"]
            for col, value in zip(cols, creds.values()):
                sql_creds[col] = value
        return sql_creds

    def is_connected(self):
        return self.connection.is_connected()
    
    def connect(self):
        self.connection = mysql.connector.connect(
                                            pool_name = self.poolname,
                                            pool_size = self.poolsize,
                                            **self.sql_creds
                                )
        self.connection.autocommit = True
        self.innerCursor = self.connection.cursor()
        return

    def ensure_connectivity(self):
        if not self.is_connected():
            self.connect()
        return
    
    def get_results(self):
        results = None
        try:
            results = self.innerCursor.fetchall()
        except:
            pass
        return results

    def query(self, q, params):
        self.ensure_connectivity()
        self.innerCursor.execute(q, params)
        return self.get_results()

    def safe_query(self, q, params):
        self.ensure_connectivity()
        self.innerCursor.execute(query_constraint(q, params))
        return self.get_results()
    
    def close(self):
        self.connection.close()
        return







if __name__ == "__main__":
    connection = Connection(creds = "./creds/SQL") #suggested to not store creds on a file and rather user env vars. (Here only for demonstration purposes).
    user = connection.query("SELECT * FROM users WHERE uname = %(username)s;", {"username": "uchihamadara"})
    print(user)
    user = connection.query("SELECT * FROM users WHERE uname = %s;", ["uchihamadara",])
    print(user)
    user = connection.query("SELECT * FROM users WHERE uname = %s;", ("uchihamadara", ))
    print(user)