Feature: Carrinho de compras
  Como usuário
  Eu quero adicionar e remover itens do meu carrinho de compras
  Para gerenciar minhas compras

  Scenario: Adicionar itens ao carrinho
    Given que tenho um carrinho de compras com item "Camiseta" e preço R$ 29.99
    When eu adiciono o item "Calça" com o preço R$ 49.99
    Then o total do carrinho de compras deve ser R$ 79.98

  Scenario: Remover item do carrinho
    Given que tenho um carrinho de compras com item "Camiseta" e preço R$ 29.99
    When eu removo o item do carrinho
    Then o carrinho de compras deve estar vazio