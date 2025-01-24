import Image from "next/image";

export default function Home() {
  return (
    <div className="cabecalho font-[family-name:var(--font-geist-sans)]">
      <header>
        
        <Image
          className=""
          src="/next.svg"
          alt="Test logo"
          width={180}
          height={38}
          priority
        />
        
        <nav>
          <ul>
            <a href="#">
              <li>Início</li>
            </a>
            <a href="#">
              <li>Serviços</li>
            </a>
            <a href="#">
              <li>Quem Somos</li>
            </a>
            <a href="#">
              <li>Contato</li>
            </a>
          </ul>
        </nav>

        <div className= "button">
          <a href="#">
              <Image
                className="user"
                src="/file.svg"
                alt="Usuário"
                width={20}
                height={20}
              />
              <button> Entrar </button>
          </a>
        </div>
      </header>
      
    </div>
  );
}
