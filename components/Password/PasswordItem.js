import React from "react";

import Button from "../UI/Button";
import classes from "./PasswordItem.module.css";

const PasswordItem = (props) => {
  const copyToClipboardHandler = (event) => {
    const passwordText = document.getElementById(props.id).innerText;
    navigator.clipboard.writeText(passwordText);
    alert("password copied to clipboard");
  };

  return (
    <div className={classes["password-item"]}>
      <span className={classes["password-display"]}>
        <h3 id={props.id}>{props.password}</h3>
      </span>
      <Button className={classes.copy} onClick={copyToClipboardHandler}>
        Copy to Clipboard
      </Button>
      <Button
        className={classes.delete}
        onClick={props.onDelete}
        value={props.id}
      >
        (-) Delete
      </Button>
    </div>
  );
};

export default PasswordItem;
