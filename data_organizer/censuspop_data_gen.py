import openpyxl,pprint

print('loading workbook...')
wb = openpyxl.load_workbook('automate_online-materials/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('saving data...')
for row in range(2, len(sheet['A']) +1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts' : 0, 'pop' : 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

for state in countyData:
    print(state+':')
    for county in countyData[state]:
        print(county,end=' ')
    print()

print('Writing results...')
resultFile = open('/Users/chanlim/Desktop/census2010.py','w')
resultFile.write('All Data :\n' + pprint.pformat(countyData).strip('{}'))
resultFile.close()
print('Finished')