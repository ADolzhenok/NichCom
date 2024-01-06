import React from "react";
import classes from "./Button.module.css";

/**
 * New Style of Button
 * 
 * @param {{object, object, object}} objects destructuring assignment of sended props 
 * @returns React Component
 */

const Button = ({ children, className, ...props }) => {
  return (
    <button {...props} className={classes[className] + " " + classes.btn}>
      {children}
    </button>
  );
};

export default Button;
