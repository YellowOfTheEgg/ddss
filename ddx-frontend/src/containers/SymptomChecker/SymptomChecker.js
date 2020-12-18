import React, { useContext } from "react";
import { SymptomCheckerContext } from "context/symptomCheckerContext";
import Stepper from "components/Stepper/Stepper";
import SymptomsInput from "./SymptomsInput";
import Summary from "./Summary";
import styles from "./symptom-checker.module.scss";

//this container wraps the steps of entering symptoms and getting results
const SymptomChecker = () => {
  const { currentStep } = useContext(SymptomCheckerContext);

  const stepsContent = {
    "Symptoms Input": <SymptomsInput />,
    Summary: <Summary />,
  };

  return (
    <div className={styles.symptomChecker}>
      <Stepper steps={Object.keys(stepsContent)} currentStep={currentStep} />
      {stepsContent[currentStep]}
    </div>
  );
};

export default SymptomChecker;
