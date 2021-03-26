## Introdução

<p style="text-indent: 20px; text-align: justify">
As características da plataforma são um processo que faz parte do ciclo de vida da Mayhel. Elas estão intimamente ligadas as características dos usuários e os critérios de usabilidade. Isso ocorre porque os critérios de usabilidade devem estar presentes dentro do sistema em si, satisfazendo assim seus objetivos. Já com base nos usuários, isso ocorre pois todo o processo de design de interface e interação leva em consideração às questões específicas do grupo de usuários que utilizarão e interagirão com o sistema. Vale ressaltar também que, segundo Courage e Baxter (2005, apud DINIZ, 2010), os requisitos dos usuários se referem tanto aos objetivos dos usuários que o software deve ser capaz de atender, como às características de um produto, onde elas definem os comportamentos e padrões levando em consideração seus usuários.
</p>

## Objetivos
Este documento tem como principal objetivo a transcrição das principais características físicas, comportamentais, funcionais, não funcionais e externas do produto de software e sua interface. Compreendendo todas essas principais características, será possível perceber muitos detalhes implícitos e explícitos do produto, fazendo assim com que se tenha um feedback importante para elucidação de problemas e resolução dos mesmos. Com base nisso, passaremos a ter um escopo de ideias que podem (e devem) ser tratados para produzir um design melhorado e ser melhor aceito pelos usuários.
Uma pequena observação fora do escopo dos objetivos, mas, ainda assim, tangente ao assunto, seria analisar a conformidade das características da plataforma com o brainstorm de desejos e necessidades dos usuários, a fim de assegurar que suas requisições estão sendo atendidas.


## Características da Plataforma PiR2
<p style="text-indent: 20px; text-align: justify">
“Cada sistema interativo possui características e peculiaridades que o tornam único e distinto dos demais.” (DINIZ, 2010). Por mais que a cada sistema tenha todas as suas particularidades, existem formas de compor e garantir que o design de interação do produto com o usuário caminhem juntos, ou seja, o usuário estará satisfeito e protegido. Características como essas vão de encontro aos critérios de usabilidade de software, mais precisamente a parte de usabilidade, que deve garantir ao usuário: facilidade de aprendizado (learnability); facilidade de recordação (memorability); eficiência (efficiency); segurança no uso (safety); e satisfação do usuário (satisfaction). Sendo assim, podemos levantar às características da plataforma com base nesses princípios, e também com  base em outros que serão vistos posteriormente.

- ### Facilidade de aprendizado
	
	* Inicialmente o sistema se apresenta confuso, com muito texto e baixa organização
	* Termos utilizados nos botões para navegação no sistema são claros e sucintos
	* Criação de um novo tópico é de fácil acesso e possui regras no cabeçalho
	* A busca por mensagens ou tópicos é extremamente simples

- ### Facilidade de recordação
	
	* O esforço para se recordar em relação a uma determinada ação é quase nulo, visto que a 	navegação é bem objetiva, sem ambiguidades.
	* Os tópicos têm descrições, o que garante um entendimento prévio antes de acessá-lo.

- ### Eficiência
	
	* A resposta do software com relação as ações do usuário são satisfatórias.
	* O sistema foi testado em vários navegadores, e manteve o desempenho.

- ### Segurança no uso
	
	* Não existe uma confirmação se o usuário realmente deseja sair ao apertar o botão de sair. 	Isso pode ser ruim, uma vez que o botão não está distante de outros botões usuais.
	* Enquanto um usuário está redigindo algum tópico ou mensagem, e ele deseja mudar de 	guia, atualizar a página ou sair da tela (acidentalmente ou não), o sistema pergunta.

- ### Satisfação do usuário

	Níveis de satisfação: péssimo, ruim, regular, bom, ótimo
	
	* Visual - Regular
	* Padrões de formatação - Ruim
	* Sobreposição de atividades por anúncios - ruim
	* Padrões de acessibilidade – Péssimo

## Características da Plataforma PiR2 com base nas heurísticas de usabilidade

- ### Visibilidade do estado do sistema

  * O sistema é fluído e rápido na realização das atividades, o que supri em tese a necessidade de mensagens informando o estado do sistema e da atividade.

- ### Correspondência entre sistema e o mundo real

  * O sistema é orientado à expressões e conceitos populares

- ### Consistência e padronização

  * Não há ambiguidade entre os nomes que definem as atividades do sistema

- ### Flexibilidade e eficiência do uso

  * O sistema não permite customização da interface, o que pode gerar perda de produtividade

- ### Projeto estético e minimalista

  * O sistema é bem minimalista, mas a ponto de ser visualmente cansativo. Há algumas informações que não são objetivas e que não acrescentam no objetivo do sistema, bem como: data e hora atual, última visita, informações sobre usuários online, registrados e demais informações que deveriam competir apenas ao sistema em si.

- ### Ajuda e documentação

  * Existe uma guia de regras e não foi encontrada documentação, porém há uma espécie de suporte que atende via e-mail para eventuais dúvidas.

## Portablidade

Portabilidade é uma das características de qualidade contidas nas normas ISO/IEC 25010. Compreende-se por portabilidade, segundo a ISO 25010, como sendo: “Grau de eficácia e eficiência com que um sistema, produto ou componente pode ser transferido de um hardware, software ou outro ambiente operacional ou de uso para outro”. [1]

- O sistema em si foi verificado em três navegadores (Chrome, Chromium e FireFox), onde um deles apresentou discrepância no visual, apenas. No mais, a adaptabilidade e a instalabilidade seguem os padrões de qualidade da ISO 25010.
- O sistema mobile é visualmente atraente, mas do que a versão para desktop. Alguns problemas foram encontrados: maior lentidão na realização de requisições e anúncios se sobrepõe em alguns momentos recursos importantes, como a opção de login.

## Tecnologias utilizadas

![Captura de tela de 2021-03-26 01-32-40](https://user-images.githubusercontent.com/48694290/112577631-75dd8600-8dd3-11eb-9d0a-47ca124a900d.png)

Gerado por: Wappalyzer

## Conclusão

O sistema PiR2 assim como todas os produtos de software tem suas particularidades. Isso se dá principalmente pelos grupos de usuários e seus interesses, que moldam e definem as estruturas, comportamentos e características do sistema. Suas tecnologias se baseiam em ferramentas atuais do mercado, para garantir maior comodidade, segurança e confiabilidade


## Versionamento
| Versão | Data | Modificação | Autor |
|--|--|--|--|
| 1.0 | 25/03/2021 | Principais características | Ailton Aires |
| 1.1 | 26/03/2021 | Portabilidade e Conclusão | Ailton Aires |

# Referências
  
  [1] ISO / IEC 25010. ISO 25000, 2011. Disponível em: [https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=6]. Acesso em: 25 de março de 2021.
  BARBOSA, Simone; DINIZ, Bruno. Interação Humano-Computador, Editora Elsevier, Rio de Janeiro, 2010.
</p>
