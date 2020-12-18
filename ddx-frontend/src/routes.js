import React, { useState, useEffect, useContext } from "react";
import { BrowserRouter, Route, Redirect } from "react-router-dom";
import { SymptomCheckerProvider } from "context/symptomCheckerContext";
import "styles/index.scss";
import styles from "./app.module.scss";
import Header from "components/Header/Header";

import SymptomChecker from "containers/SymptomChecker/SymptomChecker";
import Login from "containers/Login/Login";
import Registration from "containers/Registration/Registration";
import AuthContext from "context/AuthContext";
import Logout from "containers/Logout/Logout";

const Routes = () => {
  const [loading, setLoading] = useState(true);
  const { getUser } = useContext(AuthContext);

  useEffect(() => {
    async function verifyUser() {
      await getUser();
      setLoading(false);
    }
    verifyUser();
  }, [getUser]);

  return (
    <>
      {!loading ? (
        <BrowserRouter>
          <Redirect from="/" to="/ddx" />
          <Route path="/login" exact>
            <Login />
          </Route>
          <Route path="/registration" exact>
            <Registration />
          </Route>
          <PrivateRoute path="/ddx">
            <div className={styles.gridContainer}>
              <div className={styles.gridHeader}>
                <Header />
              </div>
              <div className={styles.gridMain}>
                <SymptomCheckerProvider>
                  <SymptomChecker />
                </SymptomCheckerProvider>
              </div>
            </div>
          </PrivateRoute>

          <PrivateRoute path="/logout" exact>
            <Logout />
          </PrivateRoute>
        </BrowserRouter>
      ) : (
        "Loading"
      )}
    </>
  );
};

// eslint-disable-next-line react/prop-types
const PrivateRoute = ({ component: Component, children, ...rest }) => {
  const { isAuthenticated } = useContext(AuthContext);

  return (
    <Route
      {...rest}
      render={(props) =>
        isAuthenticated ? (
          Component ? (
            <Component {...props} />
          ) : (
            children
          )
        ) : (
          // eslint-disable-next-line react/prop-types
          <Redirect
            to={{ pathname: "/login", state: { from: props.location } }}
          />
        )
      }
    />
  );
};

export default Routes;
