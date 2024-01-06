import React from "react";
import classes from "./Input.module.css";

/**
 * New Input Style
 * 
 * @param {{object}} objects destructuring assignment of sended props  
 * @returns React Component
 */

const Input = ({ ...props }) => {
  return (
    <div>
      <input {...props} className={classes.input} />
    </div>
  );
};

export default Input;
