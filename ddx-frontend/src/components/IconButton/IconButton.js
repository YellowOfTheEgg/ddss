import React from "react";
import { PropTypes } from "prop-types";
import styles from "./icon-button.module.scss";

//this component defines a button based on an icon
const IconButton = ({ label, icon, size, onClick }) => {
  return (
    <button
      className={`
        ${styles.iconButton}
        ${styles[icon]}
        ${styles[size]}
      `}
      onClick={onClick}
    >
      <span className={styles.label}>{label ? label : icon}</span>
    </button>
  );
};

IconButton.propTypes = {
  label: PropTypes.string,
  icon: PropTypes.string,
  size: PropTypes.string,
  onClick: PropTypes.func,
};

IconButton.defaultProps = {
  icon: "download",
  size: "md",
};

export default IconButton;
