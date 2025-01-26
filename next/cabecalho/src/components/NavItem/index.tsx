import Link from "next/link";
import "./index.css";

// Tipos das variaveis que o componente recebe | TS
export interface NavItemProps {
    url: string;
    label: string;
    isActive?: boolean;
}

export default function NavItem(props: NavItemProps) {
    return (
        <li className="nav-item">
            <Link 
                href={props.url} 
                className={`nav-link ${props.isActive ? "active" : ""}`}>
                {props.label}
            </Link>
        </li>
    );
}