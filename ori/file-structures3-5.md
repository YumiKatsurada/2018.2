### 3.5 Uma jornada de um byte

O que acontece quando um programa escreve um byte para um arquivo no disco? 
Nós sabemos o que o programa faz, (ele diz WRITE(. . .)), e nós agora sabemos algo sobre como o byte é armazenado
em um disco,  mas nós não vimos o que acontece *entre* um programa e o disco. A história toda sobre o que acontece 
aos dados entre o programa e o disco não é algo que podemos contar aqui, mas nós podemos lhe dar uma ideia de muitas 
diferentes peças de hardware e software envolvidas e muitas tarefas que devem ser feitas ao olhar para um 
exemplo de uma jornada de um byte. 

Suponha que nós queremos acrescentar um byte representando o caractere 'P' armazenado em uma variável char c para um arquivo
nomeado na variável TEXT armazenada em algum lugar em um disco. Do ponto de vista do programa, toda a jornada
que o byte irá tomar pode ser representada pela declaração

 #### WRITE(TEXT, c, 1)
 
 mas a jornada é muito mais longa do que esta simples declaração sugere.
 A declaração WRITE() resulta em uma chamada para o sistema operacional do computador, que tem a tarefa
 de garantir que o resto da jornada é completada com sucesso. 
 
