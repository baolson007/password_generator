import React from "react";

import Card from "../UI/Card";
import PasswordItem from "./PasswordItem";
import classes from "./PasswordList.module.css";

const PasswordList = (props) => {
  let pwdList = props.passwords;
  // NOTE: event.target.value === password ID

  pwdList = props.passwords.map((pwd) => (
    <ul key={pwd.key}>
      <PasswordItem onDelete={props.onDelete} id={pwd.key} password={pwd} />
    </ul>
  ));

  return <Card className={classes["password-list"]}>{pwdList}</Card>;
};

export default PasswordList;
