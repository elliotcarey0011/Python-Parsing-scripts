import pandas as pd

df = pd.read_excel('facebook3.xls')
# this will read the first sheet into df

xls = pd.ExcelFile('facebook3.xls')

# Now you can list all sheets in the file
xls.sheet_names
# ['house', 'house_extra', ...]

# to read just one sheet to dataframe:
df = pd.read_excel(file_name, sheetname="Video Metrics Total vs. Unique")

d12 = dff['Argentina (AR)'] + dff['Australia (AU)'] + dff['Austria (AT)'] + dff['Belgium (BE)'] + dff['Bosnia and Herzegovina (BA)'] + dff['Brazil (BR)'] + dff['Bulgaria (BG)'] +	['Canada (CA)'] + ['Colombia (CO)']	+ ['Czech Republic (CZ)'] +	['Denmark (DK)'] + ['Finland (FI)'] + ['France (FR)'] + ['Germany (DE)'] + ['Greece (GR)'] + ['Hungary (HU)'] +	India (IN)	Iraq (IQ)	Ireland (IE)	Italy (IT)	Kosovo (XK)	Lithuania (LT)	Luxembourg (LU)	Macedonia (MK)	Malaysia (MY)	Mexico (MX)	Morocco (MA)	Netherlands (NL)	New Zealand (NZ)	Norway (NO)	Poland (PL)	Romania (RO)	Russia (RU)	Serbia (RS)	South Africa (ZA)	South Korea (KR)	Spain (ES)	Sweden (SE)	Switzerland (CH)	Thailand (TH)	Tunisia (TN)	Turkey (TR)	United Kingdom (GB)	United States (US)	Vietnam (VN)