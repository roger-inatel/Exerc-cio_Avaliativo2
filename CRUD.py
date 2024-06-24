from database import Database


db = Database("bolt://34.230.40.121:7687", "neo4j", "sale-nickel-prerequisite")
db.drop_all()

# Questão 1
# a
renzo = db.execute_query("MATCH (t:Teacher) WHERE t.name = 'Renzo' RETURN t.ano_nasc AS BirthYear, t.cpf AS CPF")
print(renzo)

# b
profs = db.execute_query("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS Name, t.cpf AS CPF")
print(profs)

# c
city_names = db.execute_query("MATCH (c:City) RETURN c.name AS City")
print(city_names)

# d
escola = db.execute_query("MATCH (s:School) WHERE s.number BETWEEN 150 AND 550 RETURN s.name AS SchoolName, s.number AS Number, s.address AS Address")
print(escola)

# Questão 2
# a
anos = db.execute_query("MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS Youngest, MAX(t.ano_nasc) AS Oldest")
print(anos)

# b
media = db.execute_query("MATCH (c:City) RETURN AVG(c.population) AS AvgPopulation")
print(media)

# c
nameee = db.execute_query("MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS ModifiedName")
print(nameee)

# d
terceiro = db.execute_query("MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS ThirdChar")
print(terceiro)

# fecha 
db.close()