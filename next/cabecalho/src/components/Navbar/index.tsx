"use client";
import Image from "next/image";
import Link from "next/link";
import NavItem, { NavItemProps } from "../NavItem";
import "./index.css";
import { usePathname } from "next/navigation";
import { HiMiniBars3, HiMiniXMark } from "react-icons/hi2";
import { useState } from "react";

export default function Navbar() {
  const items: NavItemProps[] = [
    { url: "/", label: "Home" },
    // {url: "/produtos", label: "Produtos"},
    { url: "/sobre", label: "Quem Somos" },
    { url: "/servicos", label: "Portfólio" },
    { url: "/contato", label: "Contato" },
  ];

  const pathname = usePathname();

  const [openMenu, setOpenMenu] = useState<boolean>(false);

  return (
    <header>
      <nav className="navbar">
        <Link 
          href="/" 
          className="logo">
          <Image 
            src="/pdf.svg" 
            alt="Logo PDF" 
            width={54} 
            height={40} />
          <p className="nome">
            <span className="primeira-palavra">Protagonistas</span> do Futuro
          </p>
        </Link>

        <ul className={`nav-items ${openMenu ? "open" : ""}`}>
          {items.map((item, index) => (
            <NavItem
              key={index}
              url={item.url}
              label={item.label}
              isActive={pathname === item.url}
            />
          ))}
        </ul>

        <button className="btn-mobile" onClick={() => setOpenMenu(!openMenu)}>
            {openMenu ? <HiMiniXMark/> : <HiMiniBars3 />}
        </button>

      </nav>
    </header>
  );
}
