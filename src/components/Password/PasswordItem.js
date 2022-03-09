import React from "react";
import classes from "./PasswordItem.module.css";

const PasswordItem = (props) => {
  return (
    <div className={classes["password-item"]}>
      <span>
        <h3>{props.password}</h3>
      </span>
      <span>
        <button onClick={props.onDelete} value={props.id}>
          (-) Delete
        </button>
      </span>
    </div>
  );
};

export default PasswordItem;
