import React from "react";
import { NavLink } from "react-router-dom";
import styles from "./header.module.scss";

//this component defines the header look
const Header = () => {
  return (
    <nav className={styles.header}>
      <ul>
        <li>
          <NavLink exact to="/ddx" activeClassName={styles.active}>
            Symptom Checker
          </NavLink>
        </li>
        <li>
          <NavLink exact to="/logout" activeClassName={styles.active}>
            Logout
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Header;
