import  utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America',data))
    countries = list(map(lambda x:x['Country/Territory'],data))
    percentages = list(map(lambda x:x['World Population Percentage'],data))
    charts.generete_pie_chart(countries,percentages)

    country = input('Type country => ')
    result = utils.population_by_country(data,country)#De toda la info selecionamos un pais

    if len(result) > 0:#el resultado tiene que tener un tamanio mayor que 0 sino no hay pais
        country = result[0]
        labels,values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels,values)
    

if __name__ == '__main__':
    run()