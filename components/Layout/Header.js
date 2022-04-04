import React from "react";
import passwordImage from "../../assets/password_logo.jpg";

import classes from "./Header.module.css";

const Header = (props) => {
  return (
    <React.Fragment>
      <header className={classes.header}>
        <h1>Password Generator</h1>
      </header>
      <div className={classes["main-image"]}>
        <img src={passwordImage} alt="password art" />
      </div>
    </React.Fragment>
  );
};

export default Header;
