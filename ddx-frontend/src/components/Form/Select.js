import React from "react";
import PropTypes from "prop-types";
import { Field, ErrorMessage } from "formik";
import styles from "./form.module.scss";

//this component defines a dropdown. It is not in use now.
const Select = ({ name, placeholder, legend, options }) => {
  return (
    <fieldset className={styles.select}>
      <legend className={styles.legend}>{legend}</legend>
      <Field
        as="select"
        name={name}
        placeholder={placeholder}
        className={styles.selectField}
      >
        <option value="" disabled>
          {placeholder}
        </option>
        {options.map((option, index) => (
          <option key={index} value={option.value}>
            {option.label}
          </option>
        ))}
      </Field>
      <ErrorMessage className={styles.error} name={name} component="div" />
    </fieldset>
  );
};

Select.propTypes = {
  name: PropTypes.string.isRequired,
  placeholder: PropTypes.string.isRequired,
  legend: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(
    PropTypes.shape({
      label: PropTypes.string.isRequired,
      value: PropTypes.any.isRequired,
    }).isRequired
  ).isRequired,
};

export default Select;
