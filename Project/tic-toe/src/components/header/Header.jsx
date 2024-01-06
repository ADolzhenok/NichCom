import React from "react";
import logo from "./tic-tac-toe.png";
import classes from "./Header.module.css";

/**
 * Header of the Pages
 * 
 * @returns React Component
 */

const Header = () => {
  return (
    <div className={classes.header}>
      <h1>
        <font className={classes.blue}>T</font>i
        <font className={classes.red}>c</font>
        Tac
        <font className={classes.blue}>T</font>o
        <font className={classes.red}>e</font>
      </h1>
      <img className="image" src={logo} alt="logo" />
    </div>
  );
};

export default Header;
