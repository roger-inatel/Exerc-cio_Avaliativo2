from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://34.230.40.121:7687", "neo4j", "sale-nickel-prerequisite")
db.drop_all()


teacher_db = TeacherCRUD(db)

#criando, pesquisando e atualizado novo professor no programa
teacher_db.create("Chris Lima", 1956, "189.052.396-66")

print(teacher_db.read("Chris Lima"))

teacher_db.update("Chris Lima", "162.052.777-77")


#menu de CLI
print("Bem vindo ao banco de dados 2")

var = 0;

while(var != 5):
  #flag de escolha para menu
  var = input("O que deseja executar?"
            "1 - adicionar o professor"
            "2-  Atualizar o CPF de um professor"
            "3 - Deletar um professor"
            "4 - Dados do professor"
            "5 - sair")


  if(var == 1):
    aux_nome = input("Nome:")
    aux_data = input("Ano_de_nascimento:")
    aux_cpf = input("CPF:")
    teacher_db.create(aux_nome,aux_data,aux_cpf)


  if(var == 2):
    aux_nome = input("Nome:")
    aux_cpf = input("CPF:")
    teacher_db.update(aux_nome,aux_cpf)


  if(var == 3):
    aux_nome = input("Nome:")
    teacher_db.delete(aux_nome)


  if(var == 4):
    aux_nome = input("Nome:")
    print(teacher_db.read(aux_nome))


db.close()