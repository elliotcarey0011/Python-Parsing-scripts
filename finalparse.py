import pandas as pd

dfa = pd.read_excel("facebookoutput.xls", sheet_name=0)
dfb = pd.read_excel("facebookoutput.xls", sheet_name=2)
dfc = pd.read_excel("facebookoutput.xls", sheet_name=6)
dfd = pd.read_excel("facebookoutput.xls", sheet_name=8)
dfe = pd.read_excel("facebookoutput.xls", sheet_name=10)
dff = pd.read_excel("facebookoutput.xls", sheet_name=19)
dfg = pd.read_excel("facebookoutput.xls", sheet_name=20)
dfh = pd.read_excel("facebookoutput.xls", sheet_name=22)
dfi = pd.read_excel("facebookoutput.xls", sheet_name=9)
df1 = dfa[['Permalink','Post ID','Lifetime Post Total Impressions','Lifetime Post Total Reach', 'Lifetime Total Video Views' , 'Lifetime Unique Video Views','Lifetime Total watches at 95%','Lifetime Unique watches at 95%','Lifetime Total 30-second Views', 'Lifetime Unique 30-second Views']]
df2 = dfb[['Lifetime Post Paid Impressions', 'Lifetime Paid 30-second Views','Lifetime Paid watches at 95%']]
df3 = dfc[['clicks to play','link clicks','other clicks','photo view']]
df4 = dfd[['comment','like','share']]
df5 = dfe[['Lifetime Total 10-second views','Lifetime Unique 10-second views','Lifetime Paid 10-second views','Lifetime total video view time (in minutes)','Lifetime 10-second Views with sound on','Lifetime video views with sound on']]
df6 = dff[['Nordrhein-Westfalen - Germany','Bayern - Germany', 'Niedersachsen - Germany','Hessen - Germany','Rheinland-Pfalz - Germany','Berlin - Germany','Schleswig-Holstein - Germany','Sachsen - Germany','Hamburg - Germany', 'Baden-Wurttemberg - Germany']]
df7 = dfg[['F.13-17','F.18-24','F.25-34','F.35-44','F.45-54','F.55-64','F.65+','M.13-17','M.18-24','M.25-34','M.35-44','M.45-54','M.55-64','M.65+','U.13-17','U.18-24','U.25-34','U.35-44','U.45-54','U.55-64','U.65+']]
df8 = dfh[['Germany (DE)','Austria (AT)','Switzerland (CH)']]
df9 = dfi[['comment','like','share']]
#d12 = dff['Argentina (AR)'] + dff['Australia (AU)'] + dff['Austria (AT)'] + dff['Belgium (BE)'] + dff['Bosnia and Herzegovina (BA)'] + dff['Brazil (BR)'] + dff['Bulgaria (BG)'] + dff['Canada (CA)'] + dff['Colombia (CO)']	+ dff['Czech Republic (CZ)'] +	dff['Denmark (DK)'] + dff['Finland (FI)'] + dff['France (FR)'] + dff['Germany (DE)'] + dff['Greece (GR)'] + dff['Hungary (HU)'] + dff['India (IN)'] + dff['Iraq (IQ)'] + dff['Ireland (IE)'] + dff['Italy (IT)'] + dff['Kosovo (XK)'] + dff['Lithuania (LT)'] + dff['Luxembourg (LU)'] + dff['Macedonia (MK)'] + dff['Malaysia (MY)'] + dff['Mexico (MX)'] + dff['Morocco (MA)'] + dff['Netherlands (NL)'] + dff['New Zealand (NZ)'] + dff['Norway (NO)'] + dff['Poland (PL)'] + dff['Romania (RO)'] + dff['Russia (RU)'] + dff['Serbia (RS)'] + dff['South Africa (ZA)'] + dff['South Korea (KR)'] + dff['Spain (ES)'] + dff['Sweden (SE)'] + dff['Switzerland (CH)'] + dff['Thailand (TH)'] + dff['Tunisia (TN)'] + dff['Turkey (TR)'] + dff['United Kingdom (GB)'] + dff['United States (US)'] + dff['Vietnam (VN)']
writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer,'Sheet1', startcol=0)
df2.to_excel(writer,'Sheet1', startcol=10)
df3.to_excel(writer,'Sheet1', startcol=14)
df4.to_excel(writer,'Sheet1', startcol=19)
df5.to_excel(writer,'Sheet1', startcol=23)
df6.to_excel(writer,'Sheet1', startcol=32)
df7.to_excel(writer,'Sheet1', startcol=41)
df8.to_excel(writer,'Sheet1', startcol=63)
df9.to_excel(writer,'Sheet1', startcol=68)
writer.save()


#df9 = dfi[['comment','like','share']]
#df10 = dfip['comment'] + ['like'] + ['share']
#writer = pd.ExcelWriter('output.xlsx')