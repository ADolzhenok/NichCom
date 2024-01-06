import React from "react";
import classes from "./Arrow.module.css"

const Arrow = ({...props}) => {
    return (
        <div {...props} className={classes.arrow}>
            <div className={classes.arrowLines}></div>
        </div>
    )
}

export default Arrow;