import React, { useState, useContext } from "react";
import styles from "./login.module.scss";
import Button from "components/Button/Button";
import { gatewayApi } from "api";
import AuthContext from "context/AuthContext";
import { useHistory } from "react-router-dom";

//this container defines the view of /login endpoint
function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loginError, setLoginError] = useState("");
  const { setIsAuthenticated, Registered } = useContext(AuthContext);

  const history = useHistory();

  const onCredentialsSubmit = async () => {
    if (username === "" || password === "") {
      setLoginError("Please enter your email and your password");
    } else {
      try {
        let credentials = new FormData();
        credentials.set("username", username);
        credentials.set("password", password);

        const response = await gatewayApi.post(
          "/login/access-token",
          credentials
        );
        if (response.data["status_code"] === 200) {
          setIsAuthenticated(true);
          history.push("/ddx");
        } else {
          setLoginError(response.data.body["detail"]);
        }
      } catch (error) {
        console.log(error);
      }
    }
  };
  const onRegistration = (e) => {
    history.push("/registration");
  };

  const onUsernameChange = (e) => {
    setUsername(e.target.value);
  };
  const onPasswordChange = (e) => {
    setPassword(e.target.value);
  };

  return (
    <div className={styles.background}>
      <div className={styles.backgroundImage}>
        <h1>
          Differential<br></br>Diagnostics
        </h1>
        <h3>your personal symptoms checker</h3>
        <div className={styles.loginBox}>
          <h2>Sign in</h2>
          <p>Please enter your email and password</p>
          <p className={styles.error}>{loginError}</p>
          <p className={styles.success}>{Registered}</p>
          <div className={styles.formArea}>
            <input
              type="text"
              id="email"
              placeholder="Email"
              onChange={onUsernameChange}
              value={username}
            />
            <form>
              <input
                type="password"
                id="password"
                placeholder="Password"
                onChange={onPasswordChange}
                value={password}
                autoComplete="on"
              />
            </form>

            <Button
              label="SIGN IN"
              type="submit"
              size="sm"
              onClick={onCredentialsSubmit}
            />
          </div>
          <div style={{ textAlign: "center" }}>
            <button className={styles.link} onClick={onRegistration}>
              I want to register
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
