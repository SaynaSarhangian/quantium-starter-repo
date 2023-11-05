import pandas as pd
import dash

if __name__ == '__main__':
    files_list = [r"D:\3-repos\quantium-starter-repo\data\daily_sales_data_0.csv",
                  r"D:\3-repos\quantium-starter-repo\data\daily_sales_data_1.csv",
                  r"D:\3-repos\quantium-starter-repo\data\daily_sales_data_2.csv"]
    dfs = [pd.read_csv(file, parse_dates=['date']) for file in files_list]
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)  # (41160, 5)

    combined_df = combined_df[combined_df['product'] == 'pink morsel']  # (5880, 5)
    combined_df['price'] = combined_df['price'].str.replace('$', '').astype(float)
    # print(combined_df.dtypes)

    combined_df['sales'] = combined_df['quantity'] * combined_df['price']
    combined_df = combined_df.drop(columns=['product', 'price', 'quantity'])
    print(combined_df.head())

# product      object
# price       float64
# quantity      int64
# date         datetime64[ns]
# region       object
