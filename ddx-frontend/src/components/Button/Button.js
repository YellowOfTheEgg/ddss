import React from "react";
import { PropTypes } from "prop-types";
import styles from "./button.module.scss";


//this component contains the defined button use with its look
const Button = (props) => {
  const { label, variant, type, size, onClick, disabled, loading } = props;

  const butt_label = () => {
    if (loading === undefined || loading === false) return label;
    else {
      return (
        <div className={styles.spinner}>
          <div className={styles.bounce1}></div>
          <div className={styles.bounce2}></div>
          <div className={styles.bounce3}></div>
        </div>
      );
    }
  };

  return (
    <button
      className={`${styles.button} ${styles[variant]} ${styles[size]}`}
      onClick={onClick}
      disabled={disabled}
      type={type ? type : ""}
    >
      {butt_label()}
    </button>
  );
};

Button.propTypes = {
  label: PropTypes.string,
  variant: PropTypes.string,
  type: PropTypes.string,
  size: PropTypes.string,
  onClick: PropTypes.func,
  disabled: PropTypes.bool,
};

Button.defaultProps = {
  variant: "primary",
  size: "md",
  disabled: false,
};

export default Button;
