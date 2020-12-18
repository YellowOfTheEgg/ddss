import React from "react";
import { PropTypes } from "prop-types";
import styles from "./stepper.module.scss";


//the stepper contains only two steps right now.
//this component is shown over the caption "Symptoms Input"
const Stepper = ({ steps, currentStep }) => {
  return (
    <ol className={styles.stepper}>
      {steps.map((step, index) => (
        <li
          key={step}
          className={`
            ${styles.step}
            ${index <= steps.indexOf(currentStep) ? styles.done : styles.todo}
          `}
        >
          <span className={styles.stepTitle}>{step}</span>
        </li>
      ))}
    </ol>
  );
};

Stepper.propTypes = {
  steps: PropTypes.arrayOf(PropTypes.string),
  currentStep: PropTypes.string,
};

Stepper.defaultProps = {
  steps: ["First Step", "Second Step", "Third Step"],
  currentStep: "First Step",
};

export default Stepper;
