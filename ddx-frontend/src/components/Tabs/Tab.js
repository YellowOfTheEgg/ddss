import React from "react";
import PropTypes from "prop-types";
import styles from "./tabs.module.scss";

//definition of one tab
const Tab = ({ activeTab, label, onClick }) => {
  return (
    <li
      className={`${styles.tabItem} ${
        activeTab === label ? styles.active : ""
      }`}
      onClick={() => onClick(label)}
    >
      {label}
    </li>
  );
};

Tab.propTypes = {
  activeTab: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  onClick: PropTypes.func.isRequired,
};

export default Tab;
