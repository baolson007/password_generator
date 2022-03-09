import React, { useState } from "react";
import "./App.css";
import Header from "./components/Layout/Header";
import Button from "./components/UI/Button";
import Card from "./components/UI/Card";
import Password from "./components/Password/Password";
import PasswordList from "./components/Password/PasswordList";
import SavedPasswords from "./components/Password/SavedPasswords";

function App() {
  const [count, setCount] = useState(0);
  let [passwords, setPasswords] = useState([]);

  const deletePasswordHandler = (id) => {
    console.log("deleting item", id.target.value);
    const newPasswords = passwords.filter(
      (password) => password.key !== id.target.value
    );
    setPasswords(newPasswords);
  };

  const pwdHandler = (event) => {
    const generatedPwd = <Password key={count} count={count} />;
    console.log("key is", generatedPwd.key);

    //count modification triggers new password generation
    setCount(count + 1);
    setPasswords((prevPasswords) => {
      return [...prevPasswords, generatedPwd];
    });
  };

  return (
    <div>
      <Header />
      <div>
        <Card>
          <Button onClick={pwdHandler}>Generate Password</Button>
          <PasswordList
            passwords={passwords}
            onDelete={deletePasswordHandler}
          />
        </Card>
      </div>
    </div>
  );
}

export default App;
