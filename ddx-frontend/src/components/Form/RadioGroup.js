import React from "react";
import PropTypes from "prop-types";
import { Field, ErrorMessage } from "formik";
import styles from "./form.module.scss";


//this component defines radios. It is not in use now.
const RadioGroup = ({ name, legend, options }) => {
  return (
    <fieldset className={styles.radioGroup}>
      <legend className={styles.legend}>{legend}</legend>
      <div className={styles.options}>
        {options.map((option, index) => (
          <div key={index}>
            <Field
              className={styles.input}
              type="radio"
              name={name}
              id={option.id}
              value={option.value}
            />
            <label className={styles.label} htmlFor={option.id}>
              {option.label}
            </label>
          </div>
        ))}
      </div>
      <ErrorMessage className={styles.error} name={name} component="div" />
    </fieldset>
  );
};

RadioGroup.propTypes = {
  name: PropTypes.string.isRequired,
  legend: PropTypes.string,
  options: PropTypes.arrayOf(
    PropTypes.shape({
      label: PropTypes.string.isRequired,
      id: PropTypes.string.isRequired,
      value: PropTypes.any.isRequired,
    }).isRequired
  ).isRequired,
};

RadioGroup.defaultProps = {
  legend: "",
};

export default RadioGroup;
