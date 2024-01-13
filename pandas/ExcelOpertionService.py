import os
import matplotlib.pyplot as plt
import pandas as pd


class ExcelOpertionService:
    def __init__(self):
        pass

    @staticmethod
    def combine_multicell_phy_data(filePath, colList):
        df = pd.read_csv(filePath)
        df = pd.DataFrame(df, columns=colList + ["Cell ID"])
        df = df.sort_values(by='Time')
        rows_per_group = df['Cell ID'].nunique()
        num_rows = df.shape[0]
        remainder = num_rows % rows_per_group
        if remainder != 0:
            df = df[:-remainder]
        df['phyDlTBSize(Mbps)'] = df.groupby(df.index // rows_per_group)['phyDlTBSize(Mbps)'].transform('sum')
        df['phyUlTBSize(Mbps)'] = df.groupby(df.index // rows_per_group)['phyUlTBSize(Mbps)'].transform('sum')
        df = df.groupby(df.index // rows_per_group).first()
        df = df.drop("Cell ID", axis=1)
        return df

    @staticmethod
    def calc_rate_info(rate):
        rate_avg = sum(rate)/len(rate)
        rate_min = min(rate)
        rate_max = max(rate)
        return 'Avg: ' + str('%.3f' % rate_avg) + ' Min: ' + str('%.3f' % rate_min) + ' Max: ' + str('%.3f' % rate_max), rate_avg


    def set_excel_to_chart(self, path, testName, csvName, colList):
        filePath = ''
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.startswith(csvName):
                    filePath = os.path.join(root, f)
                    break
            if filePath != '':
                break
        if "phyDlTBSize(Mbps)" in colList or "phyUlTBSize(Mbps)" in colList:
            df = self.combine_multicell_phy_data(filePath, colList)
        else:
            df = pd.read_csv(filePath)
            # print(df.head())
            # print(df.columns)
            df = pd.DataFrame(df, columns=colList)
            df = df.sort_values(by=colList[0])
            df = df.reset_index(drop=True)
        dl, avgdl = ExcelOpertionService.calc_rate_info(df[colList[1]])
        ul, avgul = ExcelOpertionService.calc_rate_info(df[colList[2]])
        df['Time'] = df['Time'].str.split(' ').str[2]
        print(df['Time'])
        ax = df.plot(x=colList[0], title=testName + '\nUL: ' + ul + '\nDL: ' + dl, figsize=(18, 8))
        # plt.plot(df["Time"],df["DLF1u5GPdcpSendTput(Mbps)"], df["ULF1u5GPdcpRcvTput(Mbps)"])
        # plt.xticks(rotation=30)
        fig = ax.get_figure()
        # plt.show()
        fig.savefig(os.path.join(path, testName + '.png'))
        return avgdl, avgul


if __name__ == "__main__":
    eos = ExcelOpertionService()
    path = "D:/mts_auto/SinglePcc/staDataPath/MTS_21174_IM_202401041302561704345312"
    testName = "3D_4D2U_TCP_ULDL"
    csvName = "CELL_PDCP_THROUGHPUT"
    colList = ["Time", "DLF1u5GPdcpSendTput(Mbps)",	"ULF1u5GPdcpRcvTput(Mbps)"]
    eos.set_excel_to_chart(path, testName, csvName, colList)