n = int(input())

countries = list()

for _ in range(n):
    country, gold, silver, bronze = tuple(input().split())
    countries.append((int(gold), int(silver), int(bronze), country))

countries.sort(key=lambda x: x[3], reverse=False)
countries.sort(key=lambda x: x[2], reverse=True)
countries.sort(key=lambda x: x[1], reverse=True)
countries.sort(key=lambda x: x[0], reverse=True)

for country in countries:
    print(country[3] + ' ' + str(country[0]) + ' ' + str(country[1]) + ' ' + str(country[2]))