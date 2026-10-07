import os
import kagglehub
import pandas as pd
import time


class Aichatbot:
    def __init__(self):
        self.file_path = "/Users/dh/py_file/udemy/kant/cost-of-living.csv"
        self.file_name = os.path.basename(self.file_path)

    def df_setup(self):
        df = pd.read_csv(self.file_path)
        #pd.set_option('display.max_rows', None)
        #print(df.isnull().sum())
        
        df = df.fillna('Unknown')
        #print(df.iloc[80])

        def search_data_col(search, top_n):
            date_cols = df.columns[df.columns.str.contains(search, case=False, na=False)]
            results = 1

            if len(date_cols) == 0:
                #print("search results: None")
                results = None

            selected_cols = date_cols[:top_n]
            #print(f"=== '{search}' 검색 결과 열 목록 ({len(date_cols)}개 발견) ===")

            #for l in list(selected_cols):
            #    print(l, end="\n")
            
            return df[selected_cols], search, selected_cols, results

        def format_answer(results, search, selected_cols):
            if results is None:
                print("search results: None. i can't find it based on your keyword.")
                return
            else:
                print(
                    f"your keyword: {search}\n",
                    f"here's the results: \n"
                )
                if len(selected_cols) > 0:
                    for l in range(len(selected_cols)):
                        print(f"{l + 1} - {selected_cols[l]}", end="\n")
                    return print()
                else:
                    print("None.")

        def search_data_row(col, pick_cc, selected_cols):
            cc_search_option = ["country", "city"]
            for o in cc_search_option:
                mask = df[o].str.contains(pick_cc, case=False, na=False)
                if list(mask) == True:
                    break

            matched_indexes = df.index[mask]

            if len(matched_indexes) > 0:
                first_idx = matched_indexes[0]  # 첫 번째로 일치하는 행 인덱스 (예: 1)

                price = df.at[first_idx, col]
                return print(price)

        def chatbot():
            status = 1
            while status == 1:
                print(f"target csv: {self.file_name}")
                search = str(input('search keyword(ex. eggs, beer, meal...): ').lower())
                top_n = int(input('maximum number of results: '))

                results, search, selected_cols, df[selected_cols] = search_data_col(search, top_n)
                format_answer(results, search, selected_cols)

                pick_keyword = int(input("pick a number what you want to see: "))
                col = selected_cols[pick_keyword - 1]
                print(f"you picked '{selected_cols[pick_keyword - 1]}'.")
                pick_cc = str(input("type country or city you want to see: ").lower())
                time.sleep(2)
                search_data_row(col, pick_cc, selected_cols)

                repeat = input("would you like to search more?(y/n): ")
                if repeat == "n":
                    status = 0
                else:
                    continue

        chatbot()


class Poo:
    def test(self):
        df = pd.read_csv("/Users/dh/py_file/udemy/kant/cost-of-living.csv")
        print(df.shape)


if __name__ == "__main__":
    c = Aichatbot()
    c.df_setup()
    #p = Poo()
    #p.test()