from pandas import DataFrame

# / / /

def addChart(file, objects, objectsFunctions, lastChartLine, chartType):
    DataFrame({'Категория': objects, 'Значение': objectsFunctions}).to_excel(file, sheet_name = 'Лист1', startrow = lastChartLine, index = False, header = True)

    chart = file.book.add_chart({'type': chartType})
    chart.add_series({
        'categories': f'=Лист1!$A${lastChartLine + 2}:$A${lastChartLine + len(objects) + 1}',
        'values': f'=Лист1!$B${lastChartLine + 2}:$B${lastChartLine + len(objects) + 1}',
        'name': 'Значения',
    })

    file.sheets['Лист1'].insert_chart(f'D{lastChartLine + 1}', chart)
    return lastChartLine + len(objects) + (15 - len(objects) if 15 - len(objects) > 0 else 0) + 2