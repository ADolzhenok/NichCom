import React from "react";
import classes from "./Select.module.css";

/**
 * New Style of the Select
 * 
 * @param {{object, object, object}} objects destructuring assignment of sended props  
 * @returns React component
 */

const Select = ({ children, style, ...props }) => {
  return (
    <select {...props} className={classes.select}>
      {children}
    </select>
  );
};

export default Select;
