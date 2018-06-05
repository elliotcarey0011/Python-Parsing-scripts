import pandas as pd

dfa = pd.read_excel("facebook3.xls", sheet_name=0)
dfb = pd.read_excel("facebook3.xls", sheet_name=2)
dfc = pd.read_excel("facebook3.xls", sheet_name=6)
dfd = pd.read_excel("facebook3.xls", sheet_name=8)
dfe = pd.read_excel("facebook3.xls", sheet_name=9)
dff = pd.read_excel("facebook3.xls", sheet_name=19)
dfg = pd.read_excel("facebook3.xls", sheet_name=20)
dfh = pd.read_excel("facebook3.xls", sheet_name=23)
dfi = pd.read_excel("facebook3.xls", sheet_name=9)
df1 = dfa[['Permalink','Post ID','Lifetime Post Total Impressions', 'Lifetime Total Video Views' , 'Lifetime Unique Video Views','Lifetime Total 30-Second Views','Lifetime Unique 30-Second Views','Lifetime Total watches at 95%','Lifetime Unique watches at 95%']]
df2 = dfb[['Lifetime Post Paid Impressions', 'Lifetime Paid 30-Second Views','Lifetime Paid watches at 95%']]
df3 = dfc[['clicks to play','link clicks','other clicks','photo view']]
df4 = dfd[['comment','like','share']]
df5 = dfe[['Lifetime Total 10-Second Views','Lifetime Unique 10-Second Views','Lifetime Paid 10-Second Views','Lifetime Total Video View Time (in Minutes)','Lifetime 10-Second Views with sound on','Lifetime Video Views with sound on']]
df6 = dff[['Nordrhein-Westfalen - Germany','Bayern - Germany', 'Niedersachsen - Germany','Hessen - Germany','Rheinland-Pfalz - Germany','Berlin - Germany','Schleswig-Holstein - Germany','Sachsen - Germany','Hamburg - Germany']]
df7 = dfg[['F.13-17','F.18-24','F.25-34','F.35-44','F.45-54','F.55-64','F.65+','M.13-17','M.18-24','M.25-34','M.35-44','M.45-54','M.55-64','M.65+','U.13-17','U.18-24','U.25-34','U.35-44','U.45-54','U.55-64','U.65+']]
df8 = dfh[['Germany (DE)','Austria (AT)','Switzerland (CH)']]
df9 = dfi[['comment','like','share']]
df10 = dfip['comment'] + ['like'] + ['share']
writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer,'Sheet1', startcol=0)
df2.to_excel(writer,'Sheet1', startcol=10)
df3.to_excel(writer,'Sheet1', startcol=14)
df4.to_excel(writer,'Sheet1', startcol=19)
df5.to_excel(writer,'Sheet1', startcol=23)
df6.to_excel(writer,'Sheet1', startcol=29)
df7.to_excel(writer,'Sheet1', startcol=39)
df8.to_excel(writer,'Sheet1', startcol=60)
df9.to_excel(writer,'Sheet1', startcol=64)
df10.to_excel(writer,'Sheet2', startcol=0)
writer.save()