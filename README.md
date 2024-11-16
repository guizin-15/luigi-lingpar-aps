# Luigi-LingPar-APS
**APS Linguagens e Paradigmas**

---

## Motivação

A criação desta linguagem de programação tem como objetivo fornecer uma ferramenta especializada para modelar e simular cenários relacionados a fusões e aquisições (M&A) e Investment Banking (IB). Ao incorporar terminologias e conceitos específicos do setor, como `account` e `transfer`, a linguagem facilita a compreensão e manipulação de cálculos financeiros e operações comuns no mundo corporativo.

---

## Características

- **Sintaxe Simples:** A linguagem possui uma sintaxe semelhante a linguagens como C e Java, facilitando a aprendizagem para aqueles familiarizados com programação básica.
- **Palavras-chave Específicas:** Utiliza palavras-chave específicas para representar conceitos financeiros, como `account` para contas e valores monetários.
  - **`account:`** Utilizada para declarar variáveis que representam contas ou valores financeiros.
  - **`cashout:`** Para exibir valores na saída padrão.
  - **`if, else, while:`** Controle de fluxo para criar lógica condicional e loops.
- **Operações Aritméticas e Relacionais:**
  - Suporta operações como `+`, `-`, `*`, `/`.
  - Operadores relacionais como `<`, `>`, `<=`, `>=`, `==`, `!=`.
- **Escopo de Variáveis:** Variáveis possuem escopo de bloco, permitindo declarações dentro de loops e condicionais sem conflitos.

---

## Curiosidades

- **Foco em M&A e IB:** A linguagem foi projetada para refletir terminologias e operações comuns em M&A e Investment Banking, tornando-a única em seu propósito.
- **Simulação de Cenários Reais:** Permite modelar situações como cálculo de sinergias em fusões, simulação de investimentos e análise de ROI de maneira simplificada.
- **Extensível:** A estrutura da linguagem permite futuras expansões, como a implementação de funções, operações financeiras avançadas e suporte a transações complexas.

---

## Exemplos

### Declaração e Uso de Variáveis

```plaintext
account capitalInicial = 1000000;
account despesas = 200000;
account capitalLiquido;
capitalLiquido = capitalInicial - despesas;
cashout(capitalLiquido);
```

Saída: `800000`

### Uso de Condicionais
    
```plaintext            
account receita = 750000;
account custo = 800000;
account resultado;

if (receita > custo) {
    resultado = receita - custo;
    cashout(resultado);  // Lucro
} else {
    resultado = custo - receita;
    cashout(resultado);  // Prejuízo
} 
```
Saída Esperada: `50000`

### Loops e Cálculo de Juros Compostos

```plaintext 
account principal = 10000;
account taxa = 5;  // Taxa de juros em porcentagem
account anos = 10;
account i = 0;

while (i < anos) {
    principal = principal + (principal * taxa / 100);
    i = i + 1;
}
cashout(principal);
```
Saída Esperada: `16288`

## Explicação dos Testes e Fórmulas Matemáticas

### Teste 1: Variáveis Básicas

Código:
```plaintext
account initialCapital = 1000000;
account expenses = 200000;
account netCapital;
netCapital = initialCapital - expenses;
cashout(netCapital);
```
 Fórmula:

- Capital Líquido: netCapital = initialCapital - expenses

Explicação: 

- Calcula o capital restante após deduzir as despesas do capital inicial.

Saída Esperada:

- `800000`

---

### Teste 2: Juros Compostos

Código:
```plaintext
account principal = 10000;
account rate = 5;  // Taxa de juros em porcentagem
account years = 10;
account i = 0;

while (i < years) {
    principal = principal + (principal * rate / 100);
    i = i + 1;
}
cashout(principal);
```

Explicação: 

- Calcula o montante após 10 anos de juros compostos a uma taxa de 5% ao ano.

Fórmula:

- Juros Compostos: $$ A = P \times \left( 1 + \frac{r}{100} \right)^n $$

- \(P\): principal
- \(r\): taxa de juros
- \(n\): número de períodos

Cálculo:

$$
A = 10000 \times (1 + 0.05)^{10} \approx 16288
$$

Explicação:

- Calcula o montante após 10 anos de juros compostos a uma taxa de 5% ao ano.

Saída Esperada: `16288`

---

### Teste 3: Determinação de Lucro ou Prejuízo

**Código:**

```plaintext
account revenue = 750000;
account cost = 800000;
account result;

if (revenue > cost) {
    result = revenue - cost;
    cashout(result);  // Lucro
} else {
    result = cost - revenue;
    cashout(result);  // Prejuízo
}
```

Fórmula:

- Lucro: result = revenue - cost
- Prejuízo: result = cost - revenue

Explicação:

- Determina se há lucro ou prejuízo comparando a receita com o custo e calcula a diferença.

Saída Esperada: 

- `50000`

---

### Teste 4: Simulação de Múltiplas Rodadas de Investimento

Código:
```plaintext

account totalInvestment = 0;
account rounds = 5;
account i = 1;

while (i <= rounds) {
    account investment = i * 100000;  // Cada rodada aumenta o investimento
    totalInvestment = totalInvestment + investment;
    cashout(totalInvestment);
    i = i + 1;
}
cashout(totalInvestment);
```

Fórmula:
- Investimento por Rodada: investment = i * 100000
- Investimento Total: Soma dos investimentos em cada rodada

Explicação:

- Simula 5 rodadas de investimento, onde cada rodada aumenta o valor investido. Imprime o investimento total após cada rodada.

Saída Esperada: 
- `100000 
300000
600000
1000000
1500000
1500000`

--- 

Teste 5: Cálculo de Sinergias em uma Fusão

Código:

```plaintext
account companyARevenue = 500000;
account companyBRevenue = 300000;
account expectedSynergy = 200000;
account mergedRevenue;

mergedRevenue = companyARevenue + companyBRevenue + expectedSynergy;
cashout(mergedRevenue);
```

Fórmula:

- Receita Combinada: mergedRevenue = companyARevenue + companyBRevenue + expectedSynergy

Explicação:

- Calcula a receita total após a fusão de duas empresas, incluindo as sinergias esperadas.

Saída Esperada

- `1000000`

---

### Teste 6: Transferência de Fundos entre Contas

Código:
```plaintext
account accountA = 1000000;
account accountB = 500000;
account transferAmount = 200000;

// Simular transferência de accountA para accountB
if (accountA >= transferAmount) {
    accountA = accountA - transferAmount;
    accountB = accountB + transferAmount;
    cashout(accountA);
    cashout(accountB);
} else {
    cashout(0);  // Transferência falhou por fundos insuficientes
}
```

Fórmula:
- Saldo após Transferência:
- accountA = accountA - transferAmount
- accountB = accountB + transferAmount

Explicação:

- Verifica se há fundos suficientes em accountA para a transferência e atualiza os saldos de ambas as contas.

Saída Esperada:

- `800000
700000`

---

### Teste 7: Cálculo de Retorno sobre Investimento (ROI)

Código:
```plaintext
account gainFromInvestment = 150000;
account costOfInvestment = 100000;

account roi;
roi = (gainFromInvestment - costOfInvestment) * 100 / costOfInvestment;
cashout(roi);
```

Fórmula:

$
\text{ROI} = \left( \frac{\text{Ganho} - \text{Custo}}{\text{Custo}} \right) \times 100 
$

Explicação:

- Calcula o retorno percentual sobre um investimento dado o ganho e o custo.

Saída Esperada:

- `50`

---

### Teste 8: Depreciação de Ativo ao Longo do Tempo

Código:
```plaintext
account assetValue = 500000;
account depreciationRate = 10;  // Percentual ao ano
account years = 5;
account i = 0;


while (i < years) {
    assetValue = assetValue - (assetValue * depreciationRate / 100);
    i = i + 1;
    cashout(assetValue);
}
```

Fórmula:
- Depreciação Anual: assetValue = assetValue - (assetValue * depreciationRate / 100)

Explicação:

- Simula a depreciação de um ativo ao longo de 5 anos a uma taxa anual de 10%.

Saída Esperada:

- `450000
405000
364500
328050
295245`

---

### Teste 9: Análise do Ponto de Equilíbrio

Código:
```plaintext
account fixedCosts = 100000;
account variableCostPerUnit = 50;
account pricePerUnit = 100;
account units = 0;

while ((pricePerUnit * units) < (fixedCosts + variableCostPerUnit * units)) {
    units = units + 1;
}
cashout(units);
```

Fórmula:￼

$
\text{Unidades} = \frac{\text{Custos Fixos}}{\text{Preço por Unidade} - \text{Custo Variável por Unidade}} 
$

Explicação:

- Calcula o número de unidades que devem ser vendidas para cobrir todos os custos, atingindo o ponto de equilíbrio.

Cálculo:

$
\text{Unidades} = \frac{100000}{100 - 50} = 2000 
$

Saída Esperada:

- `2000`

---

### Teste 10: Crescimento de Portfólio de Ações com Reinvestimento

Código:
```plaintext
account portfolioValue = 100000;
account annualReturnRate = 7;  // Percentual ao ano
account years = 10;
account i = 0;

while (i < years) {
    portfolioValue = portfolioValue + (portfolioValue * annualReturnRate / 100);
    i = i + 1;
    cashout(portfolioValue);
}
```

Fórmula:

- Crescimento Anual: portfolioValue = portfolioValue + (portfolioValue * annualReturnRate / 100)

Explicação:

- Simula o crescimento de um portfólio de ações ao longo de 10 anos com uma taxa de retorno anual de 7%, considerando o reinvestimento dos ganhos.

Saída Esperada: 

- `107000
114490
122504
131079
140254
150071
160575
171815
183841
196710`

---

### Como Executar

	1.	Salvar o Código: Certifique-se de que o arquivo main.py contém o código completo do interpretador fornecido.
	2.	Criar Arquivos de Teste: Salve cada um dos exemplos de teste em arquivos separados com a extensão .my, por exemplo, teste1.my, teste2.my, etc.
	3.	Executar o Interpretador: No terminal, execute o interpretador passando o arquivo de teste como argumento:

`python3 main.py teste1.my`

	4.	Verificar a Saída: Compare a saída do interpretador com a saída esperada para cada teste.

### EBNF da Linguagem

Abrir arquivo EBNF.txt

---

## Conclusão

Esta linguagem de programação especializada permite modelar e simular de forma simples cenários comuns no mundo de M&A e Investment Banking. Com sintaxe intuitiva e recursos focados, é uma oportunidade de representar operações financeiras e analisar resultados.
