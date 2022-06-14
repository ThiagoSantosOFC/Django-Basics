from django.db import models

# Create your models here.
# setando as classes que serão criadas na DB como tabelas com seus respectivos campos

class cliente (models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_nome = models.CharField(max_length=100)
    cliente_endereco = models.CharField(max_length=100)
    cliente_telefone = models.CharField(max_length=100)
    cliente_email = models.CharField(max_length=100)
    cliente_data_cadastro = models.DateField()
    cliente_data_nascimento = models.DateField()
    cliente_password = models.CharField(max_length=150)
    cliente_status = models.CharField(max_length=1)
    
    def __str__(self):
        return self.cliente_nome
    
class produtos (models.Model):
    produtos_id = models.AutoField(primary_key=True)
    produto_nome = models.CharField(max_length=100)
    produto_preco = models.CharField(max_length=100)
    produto_descricao = models.CharField(max_length=120)
    produto_vendedor = models.CharField(max_length=100)
    produto_marca = models.CharField(max_length=100)
    
    def __str__(self):
        return self.produto_nome
        
class encomenda (models.Model):
    encomenda_id = models.AutoField(primary_key=True)
    encomenda_cliente_id = models.ForeignKey(cliente, on_delete=models.CASCADE) 
    encomenda_produto_id = models.ForeignKey(produtos, on_delete=models.CASCADE)                
    encomenda_data_cadastro = models.DateField()
    encomenda_data_entrega = models.DateField()
    
    
    def __str__(self):
        return self.encomenda_id
        

    
        