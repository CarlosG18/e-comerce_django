# Engenharia de Requisitos

> Descrevendo todos os requisitos que a aplicação de e-commerce COMPRONLINE irá possuir.

## 📋 Levantando os Requisitos

### ✅ Requisitos Funcionais

**🚩 Requisito 1: Sistema de Cadastro de Usuários**
- **Descrição:** O sistema deve permitir o cadastro de novos usuários (pessoa fisica e empresa).
- **Prioridade:** Alta

**🚩 Requisito 2: Sistema de Login e Autenticação**
- **Descrição:** O sistema deve permitir que os usuários façam login utilizando um email/username e senha.
- **Prioridade:** Alta

**🚩 Requisito 3: Sistema de Estoque de produtos**
- **Descrição:** O sistema deve permitir que os usuários do tipo empresa possam ter controle do estoque dos seus produtos (adicionar, remover, buscar, filtrar).
- **Prioridade:** Alta

**🚩 Requisito 4: Catálogo de Produtos**
- **Descrição:** O sistema deve exibir um catálogo de produtos com detalhes como nome, descrição, preço e disponibilidade para usuarios do tipo pessoa fisica.
- **Prioridade:** Alta

**🚩 Requisito 6: Carrinho de Compras**
- **Descrição:** O sistema deve permitir que os usuários adicionem produtos a um carrinho de compras.
- **Prioridade:** Alta

**🚩 Requisito 7: Finalização de Compra**
- **Descrição:** O sistema deve permitir que os usuários finalizem a compra, escolhendo métodos de pagamento e fornecendo informações de entrega.
- **Prioridade:** Alta

**🚩Requisito 8: Histórico de Pedidos**
- **Descrição:** O sistema deve permitir que os usuários visualizem o histórico de pedidos anteriores.
- **Prioridade:** Média

**🚩 Requisito 9: Sistema de Avaliação e Comentários de Produtos**
- **Descrição:** O sistema deve permitir que os usuários avaliem e comentem sobre os produtos adquiridos.
- **Prioridade:** Média

### 🔧 Requisitos Não Funcionais

**🚩 Requisito 1: Segurança**
- **Descrição:** O sistema deve garantir que os dados dos usuários estejam protegidos contra acessos não autorizados.
- **Prioridade:** Alta

**🚩 Requisito 2: Usabilidade**
- **Descrição:** O sistema deve ser intuitivo e fácil de usar, permitindo que novos usuários naveguem e utilizem as funcionalidades básicas sem treinamento.
- **Prioridade:** Média

## 📊 Modelagem dos Requisitos

### 🚩 Casos de Uso

#### 👤 Ator: Editor Admin

1. **📌 Editar seções**
   - **Descrição:** Permite que o editor possa fazer edições nas seções presentes na home do site.
   - **Cenário Principal:** ele poderá editar cards, textos e imagens das diversas seções que ele quiser colocar.

#### 👤 Ator: Cliente Pessoa Fisica

1. **📌 Cadastro de Usuário**
   - **Descrição:** Permite que um novo usuário crie uma conta no sistema.
   - **Cenário Principal:** Usuário fornece dados necessários (username,email,senha,cpf) e recebe uma confirmação de cadastro por email.

2. **📌 Login de Usuário**
   - **Descrição:** Permite que um usuário existente faça login no sistema.
   - **Cenário Principal:** Usuário fornece email/username e senha, sistema valida e permite o acesso a pagina principal do sistema.

3. **📌 Visualização do Catálogo de Produtos**
   - **Descrição:** Permite que o usuário navegue pelos produtos disponíveis.
   - **Cenário Principal:** Usuário acessa a página de catálogo e vê os produtos listados por categorias e empresas listadas por segmentos.

4. **📌 Adicionar Produto ao Carrinho**
   - **Descrição:** Permite que o usuário adicione um produto ao carrinho de compras.
   - **Cenário Principal:** Usuário seleciona um produto e clica em "Adicionar ao Carrinho".

5. **📌 Finalização de Compra**
   - **Descrição:** Permite que o usuário finalize a compra dos produtos no carrinho.
   - **Cenário Principal:** Usuário revisa o carrinho, escolhe o método de pagamento e fornece informações de entrega.

6. **📌 Visualização do Histórico de Pedidos**
   - **Descrição:** Permite que o usuário veja o histórico de compras feitas.
   - **Cenário Principal:** Usuário acessa a página de histórico e visualiza os pedidos anteriores.

7. **📌 Avaliação e Comentários de Produtos**
   - **Descrição:** Permite que o usuário avalie e comente sobre os produtos comprados.
   - **Cenário Principal:** Usuário acessa a página do produto e envia uma avaliação/comentário.

#### 👤 Ator: Cliente Empresa

1. **📌 Cadastro de Usuário**
   - **Descrição:** Permite que um novo usuário crie uma conta no sistema.
   - **Cenário Principal:** Usuário fornece dados necessários (username, email, senha, cnpj) e recebe uma confirmação de cadastro por email.

2. **📌 Login de Usuário**
   - **Descrição:** Permite que um usuário existente faça login no sistema.
   - **Cenário Principal:** Usuário fornece email/username e senha, sistema valida e permite o acesso a pagina principal do site do admin.

3. **📌 CRUD dos produtos**
   - **Descrição:** Permite que o usuário navegue pelos produtos.
   - **Cenário Principal:** Usuário acessa a página de edição dos produtos (admin site) onde será possivel modificar qualquer atributo do produto (preço, descrição, quantidade, etc), adicionar e remover.

4. **📌 Relatórios de vendas**
   - **Descrição:** Permite que o usuário obtenha relatorios de venda de cada produto, ou de uma categoria especifica, ou do geral.
   - **Cenário Principal:** Usuário acessa a página relatorios e seleciona o tipo de relatorio que desejar, vendas a partir de uma categoria, apenas de um produto ou de todos os produtos. o formato do relatorio será em PDF.