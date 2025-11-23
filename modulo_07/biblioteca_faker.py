from faker import Faker

fake = Faker('pt_BR')

print("Nome:", fake.name())
print("Endereço:", fake.address())
print("Email:", fake.email())
print("Telefone:", fake.phone_number())

print("Profissão:", fake.job())
print("Empresa:", fake.company())
print("CNPJ:", fake.cnpj())

print("Usuário:", fake.user_name())
print("Domínio:", fake.domain_name())
print("IP:", fake.ipv4())

print("Cidade:", fake.city())
print("Estado:", fake.state())
print("CEP:", fake.postcode())