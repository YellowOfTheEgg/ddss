import React, { createContext, useState } from "react";

export const SymptomCheckerContext = createContext();

const defaultPatientData = {
  name: "",
  info: {
    Age: "",
    Sex: "",
    Smoke: null,
    "Recent travels": null,
    Diabetis: null,
    "High blood pressure": null,
  },
};

// eslint-disable-next-line react/prop-types
export const SymptomCheckerProvider = ({ children }) => {
  //const [currentStep, setCurrentStep] = useState('Basic Info')
  const [currentStep, setCurrentStep] = useState("Symptoms Input");
  const [patient, setPatient] = useState(defaultPatientData);
  const [trueSymptoms, setTrueSymptoms] = useState([]);
  const [falseSymptoms, setFalseSymptoms] = useState([]);
  const [diagnoses, setDiagnoses] = useState([]);

  return (
    <SymptomCheckerContext.Provider
      value={{
        currentStep,
        setCurrentStep,
        patient,
        setPatient,
        trueSymptoms,
        setTrueSymptoms,
        falseSymptoms,
        setFalseSymptoms,
        diagnoses,
        setDiagnoses,
        defaultPatientData,
      }}
    >
      {children}
    </SymptomCheckerContext.Provider>
  );
};
