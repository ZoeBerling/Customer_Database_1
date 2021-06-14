"""Work in progress: download csvs of specific queries from Customer Insert Data by connecting the DAO to a tkinter canvas"""

import tkinter as tk
from Cx_InsertsDOA import CxInsertsDAO
import pandas as pd


def main():
    db = CxInsertsDAO()
    root = tk.Tk()
    create_GUI(root, db)
    root.mainloop()


class create_GUI:
    """Set up GUI"""
    def __init__(self, r, db):
        self.db = db
        self.window = r
        r.title("Customer Inserts")
        r.geometry('800x400')

        self.B = tk.Button(text = "Download CSV of unique requests",  command=self.my_fun)
        self.B.pack()

    def my_fun(self):
        df = self.db.no_duplicates()
        my_df = pd.DataFrame(df)
        my_df.to_csv('Unique_Customer_Requests.csv')
        self.B['state'] == tk.DISABLED
        self.B.config(text="Your CSV is downloading!")

        # print(df)
        # print("hi")


if __name__ == '__main__':
    main()