Minha MindSpace
===================
> Este projeto foi criado com o objetivos de (1) construir uma página de conteúdos dinâmicos na Web, (2) compreender os serviços de back-end oferecidos pelo Firebase e (3) aplicar os conhecimentos de HTML, CSS e JavaScript.


Páginas
-------------------

- Início

Tema do site: Portfólio de um Viajante

Número de Ab: 3
1. Apresentação do personagem; **camilabudke.com.br/inicio/**
2. Destinos; **camilabudke.com.br/destinos/**
3. Sobre; **camilabudke.com.br/sobre/**
4. Projetos; **projetos.camilabudke.com.br/saotomedasletras**

Subdomínios
----------
- projetos.camilabudke.com.br

// Firebase login auth com o Google: 

const provider = new GoogleAuthProvider();

const auth = getAuth();
signInWithPopup(auth, provider)
  .then((result) => {
    // This gives you a Google Access Token. You can use it to access the Google API.
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    // The signed-in user info.
    const user = result.user;
    // IdP data available using getAdditionalUserInfo(result)
    // ...
  }).catch((error) => {
    // Handle Errors here.
    const errorCode = error.code;
    const errorMessage = error.message;
    // The email of the user's account used.
    const email = error.customData.email;
    // The AuthCredential type that was used.
    const credential = GoogleAuthProvider.credentialFromError(error);
    // ...
  });

  // Fazer login redirecionando para página de login:
signInWithRedirect(auth, provider);

// Pegar o token OAuth do provedor:
getRedirectResult(auth)
  .then((result) => {
    // This gives you a Google Access Token. You can use it to access Google APIs.
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;

    // The signed-in user info.
    const user = result.user;
    // IdP data available using getAdditionalUserInfo(result)
    // ...
  }).catch((error) => {
    // Handle Errors here.
    const errorCode = error.code;
    const errorMessage = error.message;
    // The email of the user's account used.
    const email = error.customData.email;
    // The AuthCredential type that was used.
    const credential = GoogleAuthProvider.credentialFromError(error);
    // ...
  });


