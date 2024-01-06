import React from "react";
import classes from "./Frame.module.css";

/**
 * Rendering the main box in the center of the page
 * 
 * @param {{object, object}} objects destructuring assignment of sended props 
 * @returns React Component
 */

const Frame = ({ children, ...props }) => {
  return (
    <div {...props} className={classes.text}>
      {children}
    </div>
  );
};

export default Frame;
