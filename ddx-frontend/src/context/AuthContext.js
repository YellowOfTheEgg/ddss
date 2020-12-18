import React, { createContext, useState } from "react";
import { PropTypes } from "prop-types";
import { gatewayApi } from "api";
export const AuthContext = createContext();

//this container defines variables and functions which can be accessed from all children-components
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [Registered, setRegistered] = useState("");

  const getUser = async () => {
    try {
      const { data } = await gatewayApi.get("/users/me");
      if (data.body.is_active) {
        setIsAuthenticated(true);
      } else {
        setIsAuthenticated(false);
      }
    } catch (error) {
      setIsAuthenticated(false);
    }
  };

  return (
    <AuthContext.Provider
      value={{
        getUser,
        isAuthenticated,
        setIsAuthenticated,
        Registered,
        setRegistered,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

AuthProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export default AuthContext;
