import React from "react";
import PropTypes from "prop-types";
import { Field, ErrorMessage } from "formik";
import styles from "./form.module.scss";

//this component is used for entering the symptoms. Contains the definition of usage and the view
const InputText = ({ name, label, placeholder, id }) => {
  return (
    <div className={styles.inputText}>
      <label className={styles.label} htmlFor={id}>
        {label}
      </label>
      <Field
        className={styles.input}
        type="text"
        name={name}
        id={id}
        placeholder={placeholder}
      />
      <ErrorMessage className={styles.error} name={name} component="div" />
    </div>
  );
};

InputText.propTypes = {
  name: PropTypes.string.isRequired,
  label: PropTypes.string,
  placeholder: PropTypes.string,
  id: PropTypes.string.isRequired,
};

InputText.defaultProps = {
  label: "",
  placeholder: "",
};

export default InputText;
