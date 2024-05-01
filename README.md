PyGeneration é um script para criação de senhas com o modulo "random". Por questões de segurança  a própria documentação oficial do módulo random tem aviso bem claro:

"Warning: The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module."

O modulo correto para geração de senhas é "secrets" . 
