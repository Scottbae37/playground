import os
import pandas as pd


def sort(file_name):
    l = []

    comp_code_pd = pd.read_csv(file_name, engine='python')

    for i in comp_code_pd.index:
        (a, b, c, d, e) = comp_code_pd.loc[i, ['회사명', 'valuation','매수가','1차매도가','2차매도가']]
        l.append((a, b, c, d, e))

    sorted_list = sorted(l, key=lambda v: v[1])

    f = open('/home/scottbae37/git/s-rim-analysis/resource/sorted_valuation_list.csv', 'w')
    f.write(f'회사명, valuation,매수가,1차매도가,2차매도가{os.linesep}')
    for (a, b, c, d, e) in sorted_list:
        f.write(f'{a}, {b}, {c}, {d}, {e}{os.linesep}')

    f.close()


if __name__ == '__main__':
    file_name = '/home/scottbae37/git/s-rim-analysis/resource/valuation_list.csv'
    sort(file_name)
    print('Done...')
