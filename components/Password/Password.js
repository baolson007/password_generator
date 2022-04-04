import React, { useState, useEffect } from "react";
import classes from "./Password.module.css";

const Password = (props) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    //UNCOMMENT FOR PRODUCTION.
    //DUMMY ROUTE PROVIDED TO LIMIT HTTP REQUESTS TO HOST WEBSITE
    fetch("/home")
      //fetch("/dummyPassword")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        //console.log("USE_EFFECT", data);
      });
  }, [props.count]);

  return (
    <div className={classes.password}>
      {typeof data.password === "undefined" ? (
        <p>Loading...</p>
      ) : (
        data.password.map((password) => <p key={Math.random()}>{password} </p>)
      )}
    </div>
  );
};

export default Password;
