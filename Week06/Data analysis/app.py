import csv



with open("c:\\Users\\Hallan\\OneDrive\\Área de Trabalho\\Introdução em programação\\Week06\\Data analysis\\life-expectancy.csv") as data:
    life_expectancy = csv.reader(data, delimiter=',')

    country_year = 0
    country_year_amount = 0
    overall_max = ["", "", 0, 0]
    overall_min = ["", "", 0, 9999]
    average = 0
    year_max = ["", "", 0, 0]
    year_min = ["", "", 0, 0]

    year_guest = int(input("Enter the year of interest: "))
    for country_life_expectancy in life_expectancy:

        entity = str(country_life_expectancy[0])
        code = str(country_life_expectancy[1])
        year = int(country_life_expectancy[2])
        expectancy = float(country_life_expectancy[3])

        if expectancy < overall_min[3]:
            overall_min = [entity, code, year, expectancy]

        if expectancy > overall_max[3]:
            overall_max = [entity, code, year, expectancy]
        

        if year == year_guest:
            if expectancy > year_min[3]:
                year_min = [entity, code, year, expectancy]
    
            if expectancy < year_max[3]:
                year_max = [entity, code, year, expectancy]


       
            country_year_amount = country_year_amount + 1
            country_year = country_year + expectancy

    average = round(country_year / country_year_amount, 2)

    print(f"\nThe overall max life expectancy is: {overall_max[3]} from {overall_max[0]} in {overall_max[2]} ")
    print(f"The overall min life expectancy is: {overall_min[3]} from {overall_min[0]} in {overall_min[2]}\n")


    print(f"For the year {year_guest}:")
    print(f"The average life expectancy across all countries was {average}")
    print(f"The max life expectancy was in {year_max[0]} with {year_max[3]}")
    print(f"The min life expectancy was in {year_min[0]} with {year_min[3]}")
