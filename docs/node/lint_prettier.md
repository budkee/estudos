## Padronizar o código com **ESLint** e **Prettier**, siga estas etapas:

### **1. Instalar ESLint e Prettier**

Certifique-se de que **ESLint** e **Prettier** estão instalados no seu projeto e configurados corretamente:

#### **Instalação via npm/yarn**

Execute os seguintes comandos na raiz do projeto:

```bash
npm install eslint prettier eslint-config-prettier eslint-plugin-prettier --save-dev
```

Ou usando **yarn**:

```bash
yarn add eslint prettier eslint-config-prettier eslint-plugin-prettier --dev
```

---

### **2. Configurar o arquivo `.eslintrc`**

Crie ou edite o arquivo `.eslintrc` na raiz do projeto:

```json
{
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  },
  "extends": ["eslint:recommended", "plugin:prettier/recommended"],
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "rules": {
    "prettier/prettier": [
      "error",
      {
        "endOfLine": "auto",
        "singleQuote": true,
        "semi": true,
        "tabWidth": 2
      }
    ]
  }
}
```

Esse exemplo utiliza as configurações do ESLint e do Prettier em conjunto. A regra `prettier/prettier` aplica as regras de formatação do Prettier como erros.

---

### **3. Configurar o arquivo `.prettierrc`**

Crie um arquivo `.prettierrc` para as configurações específicas do Prettier:

```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "endOfLine": "auto"
}
```

### **4. Atualizar o `package.json` (opcional)**

Adicione scripts para rodar o ESLint e o Prettier no seu projeto:

```json
"scripts": {
  "lint": "eslint .",
  "format": "prettier --write ."
}
```

Agora você pode executar:

- `npm run lint`: Para verificar problemas no código.
- `npm run format`: Para formatar automaticamente o código.

---

### **5. Configurar o VSCode**

#### **Extensões**

- Instale as extensões:
  - **ESLint**
  - **Prettier - Code Formatter**

#### **Configuração do Workspace**

Adicione as configurações no arquivo `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  "files.eol": "\n"
}
```

Essa configuração:

- Habilita o formato ao salvar (`formatOnSave`) usando o Prettier.
- Valida arquivos com ESLint.
- Define que o final de linha será consistente (`\n`).

---

### **6. Verificar e Aplicar**

1. Salve um arquivo para que o VSCode formate automaticamente.
2. Execute `npm run lint` para garantir que não há problemas com as regras.
3. Corrija automaticamente os erros com:
   ```bash
   npm run lint -- --fix
   ```

Com essas configurações, o código será automaticamente padronizado e formatado ao salvar ou rodar os comandos.
