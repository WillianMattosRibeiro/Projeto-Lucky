import pandas as pd
from bs4 import BeautifulSoup
    
html_string = '''
  <table>
        <tr>
            <td> Hello! </td>
            <td> Table </td>
        </tr>
        <tr>
            <td> HI! </td>
            <td> Box </td>
        </tr>
    </table>
'''

soup = BeautifulSoup(html_string, 'lxml') # Parse the HTML as a string

table = soup.find_all('table')[0] # Grab the first table

new_table = pd.DataFrame(columns=range(0,2), index = [0]) # I know the size 

row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.append(column.get_text())
        column_marker += 1

print new_table